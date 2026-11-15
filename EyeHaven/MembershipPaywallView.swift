import StoreKit
import SwiftUI

/// 会员说明与购买。文案只写知识更新 / 好听声音 / 每周报告；不写「解锁全部功能」。
struct MembershipPaywallView: View {
    @Environment(MembershipStore.self) private var membership
    var compact: Bool = false

    @State private var gateAction: GateAction?
    @State private var showGate = false

    private enum GateAction {
        case buy(Product)
        case restore
    }

    var body: some View {
        @Bindable var membership = membership
        VStack(alignment: .leading, spacing: 14) {
            Text(AppL10n.passTitle)
                .font(.title3.weight(.bold))
                .foregroundStyle(Palette.dusk)

            Text(AppL10n.passIronLaw)
                .font(.subheadline.weight(.semibold))
                .foregroundStyle(Palette.moss)

            benefitRow(icon: "lightbulb.fill", title: AppL10n.passBenefitKnowledge, detail: AppL10n.passBenefitKnowledgeDetail)
            benefitRow(icon: "waveform", title: AppL10n.passBenefitVoice, detail: AppL10n.passBenefitVoiceDetail)
            benefitRow(icon: "doc.text.fill", title: AppL10n.passBenefitReport, detail: AppL10n.passBenefitReportDetail)

            Text(AppL10n.passFreeNote)
                .font(.caption)
                .foregroundStyle(Palette.pine.opacity(0.7))

            if membership.isMember {
                Label(AppL10n.passAlreadyMember, systemImage: "checkmark.seal.fill")
                    .font(.subheadline.weight(.semibold))
                    .foregroundStyle(Palette.moss)
            } else {
                priceButtons
            }

            Button(AppL10n.restorePurchases) {
                gateAction = .restore
                showGate = true
            }
            .font(.footnote.weight(.semibold))
            .foregroundStyle(Palette.pine)

            Text(AppL10n.passSubscribeLegal)
                .font(.caption2)
                .foregroundStyle(Palette.pine.opacity(0.55))

            if let msg = membership.statusMessage {
                Text(msg)
                    .font(.caption)
                    .foregroundStyle(Palette.gold)
            }
        }
        .padding(compact ? 0 : 16)
        .task {
            await membership.refresh()
        }
        .sheet(isPresented: $showGate) {
            ParentalGateView(
                onPass: {
                    showGate = false
                    guard let action = gateAction else { return }
                    gateAction = nil
                    Task {
                        switch action {
                        case .buy(let product):
                            await membership.purchase(product)
                        case .restore:
                            await membership.restore()
                        }
                    }
                },
                onCancel: {
                    showGate = false
                    gateAction = nil
                }
            )
            .presentationDetents([.medium])
        }
    }

    private var priceButtons: some View {
        VStack(spacing: 10) {
            if let yearly = membership.yearlyProduct {
                Button {
                    gateAction = .buy(yearly)
                    showGate = true
                } label: {
                    VStack(spacing: 2) {
                        Text(AppL10n.yearlyPrice(yearly.displayPrice))
                            .font(.headline.weight(.bold))
                        Text(AppL10n.yearlySaveHint)
                            .font(.caption2)
                    }
                    .frame(maxWidth: .infinity)
                    .padding(.vertical, 12)
                }
                .buttonStyle(HavenButtonStyle(filled: true))
                .disabled(membership.isLoading)
            }

            if let monthly = membership.monthlyProduct {
                Button {
                    gateAction = .buy(monthly)
                    showGate = true
                } label: {
                    Text(AppL10n.monthlyPrice(monthly.displayPrice))
                        .font(.subheadline.weight(.semibold))
                        .frame(maxWidth: .infinity)
                        .padding(.vertical, 10)
                }
                .buttonStyle(HavenButtonStyle(filled: false))
                .disabled(membership.isLoading)
            }

            if membership.products.isEmpty, !membership.isLoading {
                Text(AppL10n.pricePlaceholder)
                    .font(.caption)
                    .foregroundStyle(Palette.pine.opacity(0.65))
            }
        }
    }

    private func benefitRow(icon: String, title: String, detail: String) -> some View {
        HStack(alignment: .top, spacing: 12) {
            Image(systemName: icon)
                .font(.body.weight(.semibold))
                .foregroundStyle(Palette.moss)
                .frame(width: 28, height: 28)
                .background(Circle().fill(Palette.sage.opacity(0.35)))
            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(.subheadline.weight(.bold))
                    .foregroundStyle(Palette.dusk)
                Text(detail)
                    .font(.caption)
                    .foregroundStyle(Palette.pine.opacity(0.75))
            }
            Spacer(minLength: 0)
        }
        .padding(12)
        .background(
            RoundedRectangle(cornerRadius: 14, style: .continuous)
                .fill(Palette.foam.opacity(0.95))
        )
    }
}

struct MembershipPaywallSheet: View {
    @Environment(MembershipStore.self) private var membership
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            ScrollView {
                MembershipPaywallView()
                    .padding()
            }
            .background(Palette.mist.ignoresSafeArea())
            .navigationTitle(AppL10n.openMembership)
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button(AppL10n.close) { dismiss() }
                }
            }
        }
        .onChange(of: membership.isMember) { _, isMember in
            if isMember { dismiss() }
        }
    }
}
