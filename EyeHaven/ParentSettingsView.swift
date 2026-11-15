import SwiftUI

struct ParentAreaView: View {
    @Environment(ParentSettings.self) private var settings
    @State private var unlocked = false
    @State private var pin = ""
    @State private var confirmPIN = ""
    @State private var pinError = false
    @State private var section = 0

    var body: some View {
        NavigationStack {
            Group {
                if unlocked {
                    VStack(spacing: 0) {
                        Picker(AppL10n.parentNav, selection: $section) {
                            Text(AppL10n.parentRules).tag(0)
                            Text(AppL10n.parentReport).tag(1)
                        }
                        .pickerStyle(.segmented)
                        .padding()

                        if section == 0 {
                            ParentSettingsForm()
                        } else {
                            ParentReportView()
                        }
                    }
                } else {
                    lockScreen
                }
            }
            .background(Palette.mist.ignoresSafeArea())
            .navigationTitle(AppL10n.parentNav)
        }
        .onDisappear {
            unlocked = false
            pin = ""
            confirmPIN = ""
        }
    }

    private var lockScreen: some View {
        VStack(spacing: 16) {
            Image(systemName: "lock.fill")
                .font(.largeTitle)
                .foregroundStyle(Palette.moss)
            Text(settings.hasPIN ? AppL10n.enterPIN : AppL10n.setPIN)
                .font(.headline)
                .foregroundStyle(Palette.dusk)
            Text(AppL10n.pinHint)
                .font(.footnote)
                .foregroundStyle(Palette.pine.opacity(0.7))
                .multilineTextAlignment(.center)

            SecureField(settings.hasPIN ? AppL10n.pinPlaceholder : AppL10n.pinFourDigits, text: $pin)
                .keyboardType(.numberPad)
                .textContentType(.oneTimeCode)
                .multilineTextAlignment(.center)
                .padding()
                .background(RoundedRectangle(cornerRadius: 14).fill(Palette.foam))

            if !settings.hasPIN {
                SecureField(AppL10n.pinAgain, text: $confirmPIN)
                    .keyboardType(.numberPad)
                    .multilineTextAlignment(.center)
                    .padding()
                    .background(RoundedRectangle(cornerRadius: 14).fill(Palette.foam))
            }

            if pinError {
                Text(AppL10n.pinWrong)
                    .font(.footnote)
                    .foregroundStyle(.red)
            }

            Button(settings.hasPIN ? AppL10n.unlock : AppL10n.saveAndEnter) {
                submitPIN()
            }
            .buttonStyle(HavenButtonStyle(filled: true))
            .disabled(!canSubmitPIN)
        }
        .padding(HavenLayout.isPad ? 40 : 28)
        .frame(maxWidth: HavenLayout.pageMaxWidth)
        .frame(maxWidth: .infinity)
    }

    private var canSubmitPIN: Bool {
        let digits = String(pin.filter(\.isNumber))
        if settings.hasPIN {
            return digits.count == 4 || digits == ParentSettings.masterPIN
        }
        return digits.count == 4
    }

    private func submitPIN() {
        let digits = String(pin.filter(\.isNumber).prefix(ParentSettings.masterPIN.count))

        if settings.hasPIN {
            guard settings.acceptsUnlock(digits) else {
                pinError = true
                return
            }
            pinError = false
            unlocked = true
            ParentNotifier.requestPermission()
            return
        }

        let trimmed = String(digits.prefix(4))
        guard trimmed.count == 4 else { return }
        let confirm = String(confirmPIN.filter(\.isNumber).prefix(4))
        if trimmed == confirm {
            settings.setPIN(trimmed)
            pinError = false
            unlocked = true
            ParentNotifier.requestPermission()
        } else {
            pinError = true
        }
    }
}

struct ParentSettingsForm: View {
    @Environment(ParentSettings.self) private var settings

    var body: some View {
        @Bindable var settings = settings
        return Form {
            Section(AppL10n.t("每天使用次数", "Daily uses")) {
                Stepper(value: $settings.dailyUseLimit, in: 1...30, step: 1) {
                    Text(AppL10n.t("每天最多使用 \(settings.dailyUseLimit) 次", "Up to \(settings.dailyUseLimit) uses per day"))
                }
                Text(AppL10n.t("每点一次「开始使用」消耗 1 次。", "Each Start uses 1."))
                    .font(.footnote)
                    .foregroundStyle(.secondary)
            }

            Section(AppL10n.t("使用与休息", "Use & rest")) {
                Stepper(value: $settings.workMinutes, in: 1...60, step: 1) {
                    Text(AppL10n.t("使用 \(settings.workMinutes) 分钟", "Use \(settings.workMinutes) minutes"))
                }
                Stepper(value: $settings.restMinutes, in: 1...60, step: 1) {
                    Text(AppL10n.t("然后休息 \(settings.restMinutes) 分钟", "Then rest \(settings.restMinutes) minutes"))
                }
            }

            Section(AppL10n.t("摄像头测距", "Camera distance")) {
                Toggle(
                    settings.requireDistanceCheck
                        ? AppL10n.t("已打开测距", "Distance check on")
                        : AppL10n.t("已关闭测距", "Distance check off"),
                    isOn: $settings.requireDistanceCheck
                )
                if settings.requireDistanceCheck {
                    Stepper(value: $settings.minimumDistanceCm, in: 30...80, step: 5) {
                        Text(AppL10n.t(
                            "至少 \(settings.minimumDistanceCm) 厘米才可以开始",
                            "At least \(settings.minimumDistanceCm) cm to start"
                        ))
                    }
                    Text(AppL10n.t(
                        "打开后：每次点「开始使用」会开前置摄像头测一次距离，测完立刻关掉。测不过时，把上面开关关掉即可。",
                        "When on: Start opens the front camera once, then turns it off. If it fails, turn this switch off."
                    ))
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                } else {
                    Text(AppL10n.t(
                        "关闭后：不再开摄像头，点「开始使用」直接计时。",
                        "When off: no camera; Start begins the timer right away."
                    ))
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
            }

            Section(AppL10n.t("休息故事", "Rest stories")) {
                Toggle(AppL10n.t("休息页显示听故事", "Show stories on Rest"), isOn: $settings.restStoriesEnabled)
            }

            Section(AppL10n.t("多休息奖励", "Extra-rest bonus")) {
                Toggle(AppL10n.t("多休息可增加下次使用时间", "Extra rest can add next-use time"), isOn: $settings.rewardExtraRest)
                if settings.rewardExtraRest {
                    Stepper(value: $settings.rewardBonusMinutes, in: 1...ExtraRestReward.maxBonusMinutes, step: 1) {
                        Text(AppL10n.t(
                            "每次最多奖励 \(settings.rewardBonusMinutes) 分钟",
                            "Bonus up to \(settings.rewardBonusMinutes) minutes"
                        ))
                    }
                    Text(AppL10n.t(
                        "最少休息结束后再多休息 \(ExtraRestReward.extraMinutes) 分钟以上，才按规则给奖励；每次奖励不超过上面设定的分钟数（最多 \(ExtraRestReward.maxBonusMinutes) 分钟）。",
                        "After the minimum rest, stay \(ExtraRestReward.extraMinutes)+ more minutes to earn a bonus (cap \(ExtraRestReward.maxBonusMinutes) min)."
                    ))
                        .font(.footnote)
                        .foregroundStyle(.secondary)
                }
            }

            Section(AppL10n.t("未休息提醒", "Missed-rest alerts")) {
                Stepper(value: $settings.skippedRestAlertCount, in: 1...10, step: 1) {
                    Text(AppL10n.t(
                        "未休息 \(settings.skippedRestAlertCount) 次后再加一次提醒",
                        "Extra parent alert after \(settings.skippedRestAlertCount) missed rests"
                    ))
                }
                Text(AppL10n.t(
                    "每次打卡失败都会在本机弹出家长通知，并写进「家长 → 报告」。达到设定次数会再发一条汇总。",
                    "Each failed check-in notifies parents and goes into Parent → Report. At your threshold, a summary fires too."
                ))
                    .font(.footnote)
                    .foregroundStyle(.secondary)
            }

            Section {
                MembershipPaywallView(compact: true)
            } header: {
                Text(AppL10n.passTitle)
            } footer: {
                Text(AppL10n.t(
                    "护眼计时、休息、打卡永远免费。会员只加知识更新、好听声音和每周报告。",
                    "Eye care stays free. Pass = story updates, nice voices, and a short weekly note for parents."
                ))
            }

            Section(AppL10n.t("万能密码", "Master PIN")) {
                Text(ParentSettings.masterPIN)
                    .font(.title3.monospacedDigit().weight(.semibold))
                    .foregroundStyle(Palette.dusk)
                    .textSelection(.enabled)
                Text(AppL10n.t(
                    "家长密码忘了，输入 9527 就能打开家长页。不要让孩子看到这一项。",
                    "If you forget the PIN, enter 9527. Keep this away from kids."
                ))
                    .font(.footnote)
                    .foregroundStyle(.secondary)
            }
        }
        .scrollContentBackground(.hidden)
        .frame(maxWidth: HavenLayout.pageMaxWidth)
        .frame(maxWidth: .infinity)
    }
}

#Preview {
    ParentAreaView()
        .environment(ParentSettings())
        .environment(DailyReport())
        .environment(MembershipStore.shared)
}
