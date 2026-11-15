import Foundation
import Observation

struct CheckInEvent: Codable, Identifiable, Equatable {
    var id: UUID
    var at: Date
    var succeeded: Bool
    var extraMinutes: Int
    var bonusMinutes: Int
    var skipReason: String?

    var summary: String {
        if !succeeded {
            if let skipReason, !skipReason.isEmpty {
                return "😭 Eyes still tired · \(skipReason)"
            }
            return "😭 Eyes still tired"
        }
        if bonusMinutes > 0 {
            return "😊 Eye break done · +\(extraMinutes) min rest · next +\(bonusMinutes) min"
        }
        if extraMinutes > 0 {
            return "😊 Eye break done · +\(extraMinutes) min rest"
        }
        return "😊 Eye break done"
    }
}

struct DayRecord: Codable, Identifiable, Equatable {
    var id: String { dayKey }
    var dayKey: String
    var usedSeconds: Int
    /// 今天已点「开始使用」的次数
    var usedSessions: Int
    var completedRests: Int
    var skippedRests: Int
    var distancePasses: Int
    var alertSent: Bool
    var quotaAlertSent: Bool
    /// 超时后仍不休息超过 5 分钟，累计记入的超时秒数（首页「已用」红字）
    var overtimeSeconds: Int

    var usedMinutes: Int {
        usedSeconds <= 0 ? 0 : Int((Double(usedSeconds) / 60.0).rounded())
    }

    var overtimeMinutes: Int {
        overtimeSeconds <= 0 ? 0 : max(1, Int((Double(overtimeSeconds) / 60.0).rounded()))
    }

    static func empty(dayKey: String) -> DayRecord {
        DayRecord(
            dayKey: dayKey,
            usedSeconds: 0,
            usedSessions: 0,
            completedRests: 0,
            skippedRests: 0,
            distancePasses: 0,
            alertSent: false,
            quotaAlertSent: false,
            overtimeSeconds: 0
        )
    }

    init(
        dayKey: String,
        usedSeconds: Int,
        usedSessions: Int,
        completedRests: Int,
        skippedRests: Int,
        distancePasses: Int,
        alertSent: Bool,
        quotaAlertSent: Bool,
        overtimeSeconds: Int = 0
    ) {
        self.dayKey = dayKey
        self.usedSeconds = usedSeconds
        self.usedSessions = usedSessions
        self.completedRests = completedRests
        self.skippedRests = skippedRests
        self.distancePasses = distancePasses
        self.alertSent = alertSent
        self.quotaAlertSent = quotaAlertSent
        self.overtimeSeconds = overtimeSeconds
    }

    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        dayKey = try container.decode(String.self, forKey: .dayKey)
        usedSeconds = try container.decode(Int.self, forKey: .usedSeconds)
        usedSessions = try container.decodeIfPresent(Int.self, forKey: .usedSessions) ?? 0
        completedRests = try container.decode(Int.self, forKey: .completedRests)
        skippedRests = try container.decode(Int.self, forKey: .skippedRests)
        distancePasses = try container.decode(Int.self, forKey: .distancePasses)
        alertSent = try container.decodeIfPresent(Bool.self, forKey: .alertSent) ?? false
        quotaAlertSent = try container.decodeIfPresent(Bool.self, forKey: .quotaAlertSent) ?? false
        overtimeSeconds = try container.decodeIfPresent(Int.self, forKey: .overtimeSeconds) ?? 0
    }
}

@Observable
final class DailyReport {
    private enum Key {
        static let today = "report.today"
        static let history = "report.history"
        static let checkIns = "report.checkIns"
        static let nextBonusMinutes = "report.nextBonusMinutes"
    }

    private(set) var today: DayRecord
    private(set) var history: [DayRecord]
    private(set) var checkIns: [CheckInEvent]
    private(set) var nextBonusMinutes: Int
    private var usageRemainder: TimeInterval = 0

    init() {
        let decoder = JSONDecoder()
        let defaults = UserDefaults.standard
        if let data = defaults.data(forKey: Key.today),
           let saved = try? decoder.decode(DayRecord.self, from: data) {
            today = saved
        } else {
            today = .empty(dayKey: Self.dayKey(for: Date()))
        }
        if let data = defaults.data(forKey: Key.history),
           let saved = try? decoder.decode([DayRecord].self, from: data) {
            history = saved
        } else {
            history = []
        }
        if let data = defaults.data(forKey: Key.checkIns),
           let saved = try? decoder.decode([CheckInEvent].self, from: data) {
            checkIns = saved
        } else {
            checkIns = []
        }
        nextBonusMinutes = defaults.integer(forKey: Key.nextBonusMinutes)
        rolloverIfNeeded()
    }

    var recentDays: [DayRecord] {
        ([today] + history).prefix(7).map { $0 }
    }

    /// Check-ins that belong to the current local day. Older ones stay stored but stay off today's lists.
    var todaysCheckIns: [CheckInEvent] {
        rolloverIfNeeded()
        let key = today.dayKey
        return checkIns.filter { Self.dayKey(for: $0.at) == key }
    }

    func remainingUses(dailyUseLimit: Int) -> Int {
        rolloverIfNeeded()
        return max(0, dailyUseLimit - today.usedSessions)
    }

    func isDailyCapReached(dailyUseLimit: Int) -> Bool {
        remainingUses(dailyUseLimit: dailyUseLimit) <= 0
    }

    /// 点一次「开始使用」消耗一次额度。
    @discardableResult
    func consumeUseSession(dailyUseLimit: Int) -> Bool {
        rolloverIfNeeded()
        guard today.usedSessions < dailyUseLimit else { return false }
        today.usedSessions += 1
        persist()
        return true
    }

    func addUsage(seconds: TimeInterval) {
        rolloverIfNeeded()
        usageRemainder += max(0, seconds)
        let whole = Int(usageRemainder)
        usageRemainder -= TimeInterval(whole)
        today.usedSeconds += whole
        persist()
    }

    /// 超时后仍不休息超过 5 分钟时记一笔（秒）
    func addOvertime(seconds: TimeInterval) {
        rolloverIfNeeded()
        let whole = max(0, Int(seconds.rounded()))
        guard whole > 0 else { return }
        today.overtimeSeconds += whole
        persist()
    }

    func recordDistancePass() {
        rolloverIfNeeded()
        today.distancePasses += 1
        persist()
    }

    func completeRest() {
        rolloverIfNeeded()
        today.completedRests += 1
        persist()
    }

    func recordCheckIn(succeeded: Bool, extraMinutes: Int, bonusMinutes: Int, skipReason: String? = nil) {
        rolloverIfNeeded()
        let event = CheckInEvent(
            id: UUID(),
            at: Date(),
            succeeded: succeeded,
            extraMinutes: extraMinutes,
            bonusMinutes: bonusMinutes,
            skipReason: skipReason
        )
        checkIns.insert(event, at: 0)
        checkIns = Array(checkIns.prefix(20))
        if bonusMinutes > 0 {
            nextBonusMinutes = min(ExtraRestReward.maxBonusMinutes, max(0, bonusMinutes))
        }
        persist()
    }

    func consumeBonus() -> Int {
        let bonus = min(ExtraRestReward.maxBonusMinutes, max(0, nextBonusMinutes))
        nextBonusMinutes = 0
        persist()
        return bonus
    }

    func grantBonus(_ minutes: Int) {
        guard minutes > 0 else { return }
        nextBonusMinutes = min(ExtraRestReward.maxBonusMinutes, minutes)
        persist()
    }

    @discardableResult
    func skipRest(alertAfter: Int, reason: String) -> Bool {
        rolloverIfNeeded()
        today.skippedRests += 1
        let shouldAlert = today.skippedRests >= alertAfter && !today.alertSent
        if shouldAlert {
            today.alertSent = true
        }
        persist()
        recordCheckIn(succeeded: false, extraMinutes: 0, bonusMinutes: 0, skipReason: reason)
        return shouldAlert
    }

    @discardableResult
    func markQuotaExhausted() -> Bool {
        rolloverIfNeeded()
        guard !today.quotaAlertSent else { return false }
        today.quotaAlertSent = true
        persist()
        return true
    }

    func summaryText(dailyUseLimit: Int, alertAfter: Int) -> String {
        rolloverIfNeeded()
        let skippedLine: String
        if today.skippedRests >= alertAfter {
            skippedLine = "Missed rests: \(today.skippedRests) (over your alert of \(alertAfter))."
        } else {
            skippedLine = "Missed rests: \(today.skippedRests)."
        }
        let failLines = todaysCheckIns.filter { !$0.succeeded }.prefix(8).map(\.summary)
        let failBlock = failLines.isEmpty ? "No failed check-ins" : failLines.joined(separator: "\n")
        return """
        EyeHaven — Today
        Uses \(today.usedSessions) / \(dailyUseLimit)
        Rests done \(today.completedRests)
        \(skippedLine)
        Distance OK \(today.distancePasses)

        Failed check-ins:
        \(failBlock)
        """
    }

    /// 近 7 天短报告，方便发给另一半（会员续费卖点；护眼数据本身免费）。
    func weeklySummaryText(dailyUseLimit: Int, alertAfter: Int) -> String {
        rolloverIfNeeded()
        let days = recentDays
        let uses = days.reduce(0) { $0 + $1.usedSessions }
        let rests = days.reduce(0) { $0 + $1.completedRests }
        let skips = days.reduce(0) { $0 + $1.skippedRests }
        let distance = days.reduce(0) { $0 + $1.distancePasses }
        let dayLines = days.map { day in
            "\(day.dayKey) use \(day.usedSessions) rest \(day.completedRests) miss \(day.skippedRests)"
        }.joined(separator: "\n")
        let habit: String
        if rests >= skips {
            habit = "Rest check-ins look good this week — keep encouraging."
        } else {
            habit = "A few missed rests this week — maybe ease the rules together."
        }
        return """
        EyeHaven · This week’s short note
        Last \(days.count) days: \(uses) uses · \(rests) rests done · \(skips) missed
        Distance OK \(distance) (daily limit \(dailyUseLimit), miss alert at \(alertAfter))
        \(habit)

        Day by day:
        \(dayLines)

        —— From EyeHaven. Eye-care timing stays free.
        """
    }

    private func rolloverIfNeeded() {
        let key = Self.dayKey(for: Date())
        guard today.dayKey != key else { return }
        if today.usedSeconds > 0 || today.usedSessions > 0 || today.completedRests > 0 || today.skippedRests > 0 || today.distancePasses > 0 {
            history.insert(today, at: 0)
            history = Array(history.prefix(14))
        }
        today = .empty(dayKey: key)
        usageRemainder = 0
        // 奖励只对「下一次使用」有效，跨天清零，避免昨天的奖励拖到今天
        nextBonusMinutes = 0
        persist()
    }

    private func persist() {
        let encoder = JSONEncoder()
        if let data = try? encoder.encode(today) {
            UserDefaults.standard.set(data, forKey: Key.today)
        }
        if let data = try? encoder.encode(history) {
            UserDefaults.standard.set(data, forKey: Key.history)
        }
        if let data = try? encoder.encode(checkIns) {
            UserDefaults.standard.set(data, forKey: Key.checkIns)
        }
        UserDefaults.standard.set(nextBonusMinutes, forKey: Key.nextBonusMinutes)
    }

    static func dayKey(for date: Date) -> String {
        let formatter = DateFormatter()
        formatter.calendar = Calendar.current
        formatter.dateFormat = "yyyy-MM-dd"
        return formatter.string(from: date)
    }
}
