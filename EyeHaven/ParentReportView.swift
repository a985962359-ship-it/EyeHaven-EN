import SwiftUI

struct ParentReportView: View {
    @Environment(ParentSettings.self) private var settings
    @Environment(DailyReport.self) private var report
    @Environment(MembershipStore.self) private var membership
    @State private var showMembership = false

    var body: some View {
        let today = report.today
        let overAlert = today.skippedRests >= settings.skippedRestAlertCount

        ScrollView {
            VStack(alignment: .leading, spacing: 16) {
                weeklyReportCard

                if today.quotaAlertSent {
                    quotaBanner
                }
                if overAlert {
                    alertBanner
                }

                HStack(spacing: 12) {
                    statCard(
                        title: AppL10n.t("今日使用", "Used today"),
                        value: AppL10n.t("\(today.usedSessions) 次", "\(today.usedSessions)"),
                        detail: AppL10n.t("上限 \(settings.dailyUseLimit) 次", "Limit \(settings.dailyUseLimit)")
                    )
                    statCard(
                        title: AppL10n.t("还剩", "Left"),
                        value: leftoverText,
                        detail: AppL10n.t("次数用完后不能再开始", "No more starts when empty")
                    )
                }

                HStack(spacing: 12) {
                    statCard(
                        title: AppL10n.t("完成休息", "Rests done"),
                        value: AppL10n.t("\(today.completedRests) 次", "\(today.completedRests)"),
                        detail: AppL10n.t("留在休息页直到结束", "Stay on Rest until it ends")
                    )
                    statCard(
                        title: AppL10n.t("未休息", "Missed"),
                        value: AppL10n.t("\(today.skippedRests) 次", "\(today.skippedRests)"),
                        detail: overAlert
                            ? AppL10n.t("已超过 \(settings.skippedRestAlertCount) 次", "Over \(settings.skippedRestAlertCount)")
                            : AppL10n.t("阈值 \(settings.skippedRestAlertCount) 次", "Alert at \(settings.skippedRestAlertCount)")
                    )
                }

                statCard(
                    title: AppL10n.t("测距通过", "Distance OK"),
                    value: AppL10n.t("\(today.distancePasses) 次", "\(today.distancePasses)"),
                    detail: settings.requireDistanceCheck
                        ? AppL10n.t("每次开始使用前", "Before each Start")
                        : AppL10n.t("当前未开启测距", "Distance check off")
                )

                if !failedCheckIns.isEmpty {
                    Text(AppL10n.t("眼睛休息失败记录", "Missed rest log"))
                        .font(.headline)
                        .foregroundStyle(Palette.dusk)
                        .padding(.top, 8)

                    ForEach(failedCheckIns) { event in
                        HStack(alignment: .top) {
                            Text(event.at, format: .dateTime.hour().minute())
                                .font(.subheadline.monospacedDigit())
                                .foregroundStyle(Palette.pine)
                            Spacer()
                            Text(event.summary)
                                .font(.footnote)
                                .foregroundStyle(.orange)
                                .multilineTextAlignment(.trailing)
                        }
                        .padding(12)
                        .background(
                            RoundedRectangle(cornerRadius: 14, style: .continuous)
                                .fill(Palette.foam)
                                .overlay(
                                    RoundedRectangle(cornerRadius: 14, style: .continuous)
                                        .strokeBorder(Color.orange.opacity(0.25), lineWidth: 1)
                                )
                        )
                    }
                }

                Text(AppL10n.t("近 7 天", "Last 7 days"))
                    .font(.headline)
                    .foregroundStyle(Palette.dusk)
                    .padding(.top, 8)

                ForEach(report.recentDays) { day in
                    HStack(spacing: 10) {
                        Text(day.dayKey)
                            .font(.subheadline.monospacedDigit().weight(.semibold))
                            .foregroundStyle(Palette.dusk)
                        Spacer()
                        dayChip(AppL10n.t("用 \(day.usedSessions)", "Use \(day.usedSessions)"), color: Palette.moss)
                        dayChip(AppL10n.t("休 \(day.completedRests)", "Rest \(day.completedRests)"), color: Palette.pine)
                        dayChip(
                            AppL10n.t("跳 \(day.skippedRests)", "Miss \(day.skippedRests)"),
                            color: day.skippedRests >= settings.skippedRestAlertCount
                                ? Color(red: 0.75, green: 0.3, blue: 0.2)
                                : Palette.pine.opacity(0.55)
                        )
                    }
                    .padding(12)
                    .background(
                        RoundedRectangle(cornerRadius: 14, style: .continuous)
                            .fill(Palette.foam)
                    )
                }
            }
            .padding(HavenLayout.isPad ? 28 : 16)
            .frame(maxWidth: HavenLayout.pageMaxWidth)
            .frame(maxWidth: .infinity)
        }
        .sheet(isPresented: $showMembership) {
            MembershipPaywallSheet()
                .environment(membership)
        }
    }

    /// 本周短报告：护眼数据免费看；分享在收费开启后作为会员权益。
    private var weeklyReportCard: some View {
        let text = report.weeklySummaryText(
            dailyUseLimit: settings.dailyUseLimit,
            alertAfter: settings.skippedRestAlertCount
        )
        let canShare = membership.isMember || !membership.billingReady

        return VStack(alignment: .leading, spacing: 10) {
            Text(AppL10n.t("本周短报告", "This week’s short note"))
                .font(.headline)
                .foregroundStyle(Palette.dusk)
            Text(AppL10n.t(
                "一张短文，方便发给另一半。护眼计时本身永远免费。",
                "A short note for a co-parent. The eye-care timer stays free."
            ))
                .font(.caption)
                .foregroundStyle(Palette.pine.opacity(0.7))

            Text(text)
                .font(.footnote)
                .foregroundStyle(Palette.pine)
                .padding(12)
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(RoundedRectangle(cornerRadius: 12).fill(Palette.foam))

            if canShare {
                ShareLink(item: text) {
                    Label(AppL10n.t("分享给家人", "Share with family"), systemImage: "square.and.arrow.up")
                        .font(.subheadline.weight(.semibold))
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 10)
                }
                .buttonStyle(HavenButtonStyle(filled: true))
            } else {
                Button {
                    showMembership = true
                } label: {
                    Text(AppL10n.t(
                        "开通会员后可一键分享（会员含知识更新与好听声音）",
                        "Share with the Pass (includes story updates & nice voices)"
                    ))
                        .font(.subheadline.weight(.semibold))
                        .multilineTextAlignment(.center)
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 10)
                }
                .buttonStyle(HavenButtonStyle(filled: false))
            }
        }
        .padding(14)
        .background(
            RoundedRectangle(cornerRadius: 16, style: .continuous)
                .fill(Palette.sage.opacity(0.35))
        )
    }

    private var leftoverText: String {
        let left = report.remainingUses(dailyUseLimit: settings.dailyUseLimit)
        return AppL10n.t("\(left) 次", "\(left)")
    }

    private var failedCheckIns: [CheckInEvent] {
        report.todaysCheckIns.filter { !$0.succeeded }
    }

    private var quotaBanner: some View {
        HStack(alignment: .top, spacing: 10) {
            Image(systemName: "bell.fill")
            Text(AppL10n.t(
                "今天额度已用完，使用报告已通知家长。",
                "Today’s uses are gone. Parents were notified."
            ))
                .font(.subheadline.weight(.medium))
        }
        .foregroundStyle(Palette.foam)
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(RoundedRectangle(cornerRadius: 16).fill(Palette.pine))
    }

    private var alertBanner: some View {
        HStack(alignment: .top, spacing: 10) {
            Image(systemName: "exclamationmark.triangle.fill")
            Text(AppL10n.t(
                "孩子今天多次没有完成休息，请看看使用习惯。",
                "Several missed rests today — check screen habits."
            ))
                .font(.subheadline.weight(.medium))
        }
        .foregroundStyle(.white)
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(RoundedRectangle(cornerRadius: 16).fill(Color.orange.opacity(0.9)))
    }

    private func dayChip(_ text: String, color: Color) -> some View {
        Text(text)
            .font(.caption2.weight(.bold))
            .foregroundStyle(color)
            .padding(.horizontal, 8)
            .padding(.vertical, 4)
            .background(Capsule().fill(color.opacity(0.12)))
    }

    private func statCard(title: String, value: String, detail: String) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(title)
                .font(.caption)
                .foregroundStyle(Palette.pine.opacity(0.7))
            Text(value)
                .font(.title3.weight(.semibold))
                .foregroundStyle(Palette.dusk)
            Text(detail)
                .font(.caption2)
                .foregroundStyle(Palette.moss)
        }
        .padding(14)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(
            RoundedRectangle(cornerRadius: 16, style: .continuous)
                .fill(Palette.foam)
                .shadow(color: Palette.pine.opacity(0.05), radius: 4, y: 2)
        )
    }
}
