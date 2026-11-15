import Foundation

/// 美国英文版：界面与内容库固定英文（与中文 EyeHaven 工程分开）。
enum AppL10n {
    static var isEnglish: Bool { true }

    static func t(_ zh: String, _ en: String) -> String {
        isEnglish ? en : zh
    }

    // MARK: - Tabs / Home

    static var tabTimer: String { t("眼睛闹钟", "Timer") }
    static var tabStories: String { t("睡前故事", "Stories") }
    static var tabParent: String { t("家长设置", "Parent") }

    static var homeTitle: String { t("护眼计时", "Eye Break Timer") }
    static var remainingCaption: String { t("剩余", "Left") }
    static var used: String { t("已用", "Used") }
    static var rested: String { t("休息", "Rests") }
    static var skipped: String { t("未休息", "Missed") }
    static var pause: String { t("暂停", "Pause") }
    static var resume: String { t("继续", "Resume") }
    static var toHomeScreen: String { t("去桌面", "Home Screen") }
    static var startUse: String { t("开始使用", "Start") }

    static func overtimeMinutes(_ n: Int) -> String {
        t("超时\(n)分", "+\(n) min late")
    }

    static func nextBonus(_ n: Int) -> String {
        t("下次使用奖励 +\(n) 分钟", "Next use bonus +\(n) min")
    }

    static func headerDetail(work: Int, rest: Int, distanceOn: Bool, cm: Int) -> String {
        let dist = distanceOn
            ? t("测距 \(cm) 厘米", "Distance \(cm) cm")
            : t("未开测距", "No distance check")
        return t(
            "用 \(work) 分 · 休息 \(rest) 分 · \(dist)",
            "\(work) min use · \(rest) min rest · \(dist)"
        )
    }

    // MARK: - Rest page

    static var restSuccess: String { t("😊 爱眼成功", "Eye break done") }
    static var restFinishFirst: String { t("先把休息做完", "Finish this rest first") }
    static var restBonusSaving: String { t("可以继续歇，奖励正在攒", "Keep resting — bonus building") }
    static var restingLookFar: String { t("休息中 看窗外远处可以保护眼睛", "Resting — look far away") }
    static var listenEyesClosed: String { t("闭上眼睛听", "Close your eyes and listen") }
    static var tapPlayToListen: String { t("点播放才开始听", "Tap Play to listen") }
    static var nextStory: String { t("下一则", "Next") }
    static var play: String { t("播放", "Play") }

    // MARK: - Membership

    static var passTitle: String { t("光光知识会员", "Guangguang Learning Pass") }
    static var passIronLaw: String {
        t(
            "护眼计时、休息、打卡永远免费。会员只加学习内容。",
            "Eye-care timer, rest, and check-in stay free forever. The Pass only adds learning."
        )
    }
    static var passBenefitKnowledge: String { t("知识连载更新", "Story updates") }
    static var passBenefitKnowledgeDetail: String {
        t("为什么、人物、寻宝、安全完整听", "Why, people, treasure, and safety — full listens")
    }
    static var passBenefitVoice: String { t("好听的声音", "Nice voices") }
    static var passBenefitVoiceDetail: String {
        t("优先用录好的声音陪听", "Prefer recorded voices while you listen")
    }
    static var passBenefitReport: String { t("每周家长报告", "Weekly parent note") }
    static var passBenefitReportDetail: String {
        t("一张短报告，方便发给另一半", "A short note you can share with a co-parent")
    }
    static var passFreeNote: String {
        t(
            "免费可试听每书架前几篇；目录标题都能看。故事书架会多留几篇免费。",
            "Free full listens for the first few on each shelf. All titles stay visible. Story shelves keep a few more free."
        )
    }
    static var passAlreadyMember: String { t("你已是会员", "You’re a member") }
    static var restorePurchases: String { t("恢复购买", "Restore Purchases") }
    static var passSubscribeLegal: String {
        t(
            "订阅由苹果账户扣款，可随时在系统「订阅」里取消。取消后当期结束前仍可用。",
            "Billed to your Apple ID. Cancel anytime in Subscriptions. Access lasts until the period ends."
        )
    }
    static var openMembership: String { t("开通会员", "Get the Pass") }
    static var close: String { t("关闭", "Close") }

    static func yearlyPrice(_ price: String) -> String {
        t("年费 \(price)", "Yearly \(price)")
    }
    static var yearlySaveHint: String {
        t("更省 · 约合每月不到 7 元", "Best value · nearly half off vs monthly")
    }
    static func monthlyPrice(_ price: String) -> String {
        t("月费 \(price)", "Monthly \(price)")
    }
    static var pricePlaceholder: String {
        t(
            "价格：月费约 9.9 元，年费约 78 元。商品上架后这里可直接购买。",
            "About $3.99 / month or $24.99 / year. Buy here once products are live in the store."
        )
    }

    static var storeNotReady: String {
        t(
            "订阅商品还没在苹果后台上架，先都能听。上架后自动按免费额度试听。",
            "Store products aren’t live yet — everything plays for now. Free quotas apply once products appear."
        )
    }
    static var storeOffline: String {
        t("暂时连不上商店，先都能听。", "Can’t reach the store — everything plays for now.")
    }
    static var memberActivated: String {
        t("会员已开通。护眼功能仍一直免费。", "Pass active. Eye-care features stay free.")
    }
    static var purchasePending: String {
        t("购买待确认，请稍后再看会员状态。", "Purchase pending. Check membership again soon.")
    }
    static var purchaseFailed: String {
        t("购买没成功，请稍后重试。", "Purchase didn’t finish. Please try again.")
    }
    static var restoreOK: String { t("已恢复会员。", "Membership restored.") }
    static var restoreNone: String { t("没有找到可恢复的会员。", "No membership found to restore.") }
    static var restoreFailed: String {
        t("恢复失败，请检查网络后重试。", "Restore failed. Check the network and try again.")
    }

    // MARK: - Parent

    static var parentNav: String { t("家长", "Parent") }
    static var parentRules: String { t("规则", "Rules") }
    static var parentReport: String { t("报告", "Report") }
    static var enterPIN: String { t("输入家长密码", "Enter parent PIN") }
    static var setPIN: String { t("设置 4 位家长密码", "Set a 4-digit parent PIN") }
    static var pinHint: String {
        t(
            "规则和报告都在这里。密码只保存在这台设备上。",
            "Rules and reports live here. The PIN stays on this device only."
        )
    }
    static var pinPlaceholder: String { t("家长密码或万能密码", "Parent PIN or master PIN") }
    static var pinFourDigits: String { t("4 位数字", "4 digits") }
    static var pinAgain: String { t("再输入一次", "Enter again") }
    static var pinWrong: String { t("密码不对，请重试。", "Wrong PIN. Try again.") }
    static var unlock: String { t("解锁", "Unlock") }
    static var saveAndEnter: String { t("保存并进入", "Save & Enter") }

    // MARK: - Parental gate

    static var parentalGateTitle: String { t("请家长完成", "Parent check") }
    static var parentalGateHint: String {
        t("购买和恢复需要家长答一道简单题。", "Buying or restoring needs a quick parent question.")
    }
    static var parentalGateCancel: String { t("取消", "Cancel") }
    static var parentalGateOK: String { t("确认", "OK") }
    static var parentalGateWrong: String { t("不对，再试一次。", "Not quite — try again.") }

    // MARK: - Session headlines (display only)

    static var readyToStart: String { t("准备开始", "Ready") }
    static var dailyUsesGone: String { t("今天的使用次数用完了", "Today’s uses are used up") }
    static var inUse: String { t("使用中", "In use") }
    static var paused: String { t("已暂停", "Paused") }
    static var openRestPage: String { t("请打开休息页打卡", "Open the Rest page") }
    static var restingCheckIn: String { t("休息打卡中", "Rest check-in") }
    static var canKeepResting: String { t("可以继续休息", "You can keep resting") }

    static func minutesOnly(_ minutes: Int) -> String {
        t("\(minutes)分", "\(minutes)m")
    }

    // MARK: - Shelves (UI labels)

    static func ageTitle(id: String, fallback: String) -> String {
        switch id {
        case "child": return t("儿童类", "Ages 3–10")
        case "youth": return t("少年类", "Ages 11–15")
        default: return fallback
        }
    }

    static func shelfTitle(id: String, fallback: String) -> String {
        switch id {
        case "animals": return "Animals"
        case "why": return "Why?"
        case "body": return "My Body"
        case "space": return "Space"
        case "how": return "How Things Work"
        case "weather": return "Sky & Weather"
        case "earth": return "Earth & Nature"
        case "safety": return "Safety Theater"
        // Legacy keys from older builds
        case "knowledge": return "Why?"
        case "fairy": return "Stories"
        case "biography": return "People"
        case "treasure": return "Places"
        default: return fallback
        }
    }

    static func shelfBadge(id: String, fallback: String) -> String {
        switch id {
        case "animals": return "Animals"
        case "why": return "Why"
        case "body": return "Body"
        case "space": return "Space"
        case "how": return "How"
        case "weather": return "Sky"
        case "earth": return "Earth"
        case "safety": return "Safety"
        case "knowledge": return "Why"
        case "fairy": return "Stories"
        case "biography": return "People"
        case "treasure": return "Places"
        default: return fallback
        }
    }
}
