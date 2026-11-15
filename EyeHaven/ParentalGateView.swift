import SwiftUI

/// 家长关卡：购买 / 恢复购买前答简单加法。孩子侧不能直接付。
struct ParentalGateView: View {
    var onPass: () -> Void
    var onCancel: () -> Void

    @State private var a = 0
    @State private var b = 0
    @State private var answer = ""
    @State private var wrong = false

    var body: some View {
        NavigationStack {
            VStack(spacing: 20) {
                Text(AppL10n.parentalGateTitle)
                    .font(.title3.weight(.bold))
                    .foregroundStyle(Palette.dusk)
                Text(AppL10n.parentalGateHint)
                    .font(.subheadline)
                    .foregroundStyle(Palette.pine.opacity(0.75))
                    .multilineTextAlignment(.center)

                Text("\(a) + \(b) = ?")
                    .font(.largeTitle.weight(.bold).monospacedDigit())
                    .foregroundStyle(Palette.moss)

                TextField("?", text: $answer)
                    .keyboardType(.numberPad)
                    .multilineTextAlignment(.center)
                    .font(.title2.monospacedDigit())
                    .padding()
                    .background(RoundedRectangle(cornerRadius: 14).fill(Palette.foam))

                if wrong {
                    Text(AppL10n.parentalGateWrong)
                        .font(.footnote)
                        .foregroundStyle(.red)
                }

                HStack(spacing: 12) {
                    Button(AppL10n.parentalGateCancel) { onCancel() }
                        .buttonStyle(HavenButtonStyle(filled: false))
                    Button(AppL10n.parentalGateOK) { submit() }
                        .buttonStyle(HavenButtonStyle(filled: true))
                }
            }
            .padding(28)
            .frame(maxWidth: HavenLayout.pageMaxWidth)
            .frame(maxWidth: .infinity, maxHeight: .infinity)
            .background(Palette.mist.ignoresSafeArea())
            .navigationBarTitleDisplayMode(.inline)
            .onAppear { roll() }
        }
    }

    private func roll() {
        a = Int.random(in: 2...9)
        b = Int.random(in: 2...9)
        answer = ""
        wrong = false
    }

    private func submit() {
        let n = Int(answer.filter(\.isNumber)) ?? -1
        if n == a + b {
            onPass()
        } else {
            wrong = true
            roll()
        }
    }
}
