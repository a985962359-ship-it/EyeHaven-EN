import AVFoundation
import SwiftUI

/// 点插图对话框（整泡）朗读。先试 E-A01。不改休息/计时。
@MainActor
final class ComicSentenceSpeaker: NSObject, ObservableObject {
    static let shared = ComicSentenceSpeaker()

    @Published private(set) var speakingText: String?

    private let synth = AVSpeechSynthesizer()
    private var bridge: SentenceSpeechBridge?

    private override init() {
        super.init()
        let b = SentenceSpeechBridge()
        b.owner = self
        bridge = b
        synth.delegate = b
    }

    static func isEnabled(for storyID: String) -> Bool {
        storyID == "E-A01"
    }

    func speakPhrase(_ text: String) {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty else { return }

        let player = BedtimeAudioPlayer.shared
        if player.isPlaying {
            player.togglePauseResume()
        }
        if synth.isSpeaking {
            synth.stopSpeaking(at: .immediate)
        }

        speakingText = trimmed
        let utterance = AVSpeechUtterance(string: trimmed)
        utterance.voice = Self.bestEnglishVoice()
        utterance.rate = AVSpeechUtteranceDefaultSpeechRate * 0.88
        utterance.pitchMultiplier = 1.02
        try? AVAudioSession.sharedInstance().setCategory(.playback, mode: .spokenAudio, options: [.duckOthers])
        try? AVAudioSession.sharedInstance().setActive(true)
        synth.speak(utterance)
    }

    fileprivate func didFinish() {
        speakingText = nil
    }

    private static func bestEnglishVoice() -> AVSpeechSynthesisVoice? {
        let voices = AVSpeechSynthesisVoice.speechVoices().filter { $0.language.hasPrefix("en") }
        return voices.first(where: { $0.quality == .enhanced && $0.language.hasPrefix("en-US") })
            ?? voices.first(where: { $0.language.hasPrefix("en-US") })
            ?? AVSpeechSynthesisVoice(language: "en-US")
            ?? AVSpeechSynthesisVoice(language: "en-GB")
    }
}

private final class SentenceSpeechBridge: NSObject, AVSpeechSynthesizerDelegate {
    weak var owner: ComicSentenceSpeaker?

    func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didFinish utterance: AVSpeechUtterance) {
        Task { @MainActor in owner?.didFinish() }
    }

    func speechSynthesizer(_ synthesizer: AVSpeechSynthesizer, didCancel utterance: AVSpeechUtterance) {
        Task { @MainActor in owner?.didFinish() }
    }
}

/// E-A01 气泡文案写死在代码里，避免 Bundle JSON 没打进包导致“点了没反应”。
enum ComicBubbleWordsCatalog {
    /// pageIndex 0-based → (left, right)
    private static let birds: [(String, String)] = [
        ("Why can birds fly?", "Paper ones can't!"),
        ("Hollow bones!", "Less to lift."),
        ("Strong chest.", "Wings pull hard."),
        ("Soft feathers", "catch the air."),
        ("Push air down—", "bird goes up!"),
        ("Curved wing", "rides the wind."),
        ("We're heavier.", "No wing feathers."),
        ("Planes borrow", "the same idea."),
        ("See the curve?", "Watch a turn."),
        ("Push, then coast.", "Again!"),
        ("Not magic—", "built for sky."),
        ("Count one flap.", "Smile."),
    ]

    static func bubbles(storyID: String, pageIndex: Int) -> (left: String, right: String)? {
        guard storyID == "E-A01", birds.indices.contains(pageIndex) else { return nil }
        let p = birds[pageIndex]
        return (p.0, p.1)
    }
}

/// 点左/右整块对话框区域 → 朗读该泡整句。大热区，不依赖气泡检测。
struct ComicBubbleTapOverlay: View {
    let storyID: String
    let pageIndex: Int

    @ObservedObject private var speaker = ComicSentenceSpeaker.shared

    private var phrases: (left: String, right: String)? {
        ComicBubbleWordsCatalog.bubbles(storyID: storyID, pageIndex: pageIndex)
    }

    var body: some View {
        if ComicSentenceSpeaker.isEnabled(for: storyID), let phrases {
            GeometryReader { geo in
                let w = geo.size.width
                let h = geo.size.height
                // 覆盖插图上半左右（对话框常见位置），热区够大孩子好点
                let bubbleH = max(72, h * 0.34)
                HStack(spacing: 8) {
                    bubbleButton(phrases.left, width: (w - 8) / 2, height: bubbleH)
                    bubbleButton(phrases.right, width: (w - 8) / 2, height: bubbleH)
                }
                .padding(.horizontal, 6)
                .padding(.top, 6)
                .frame(width: w, height: h, alignment: .top)
            }
            .allowsHitTesting(true)
        }
    }

    private func bubbleButton(_ text: String, width: CGFloat, height: CGFloat) -> some View {
        let active = speaker.speakingText == text
        return Button {
            speaker.speakPhrase(text)
        } label: {
            VStack(spacing: 6) {
                Image(systemName: active ? "speaker.wave.2.fill" : "speaker.wave.2")
                    .font(.title2.weight(.bold))
                Text(text)
                    .font(HavenLayout.isPad ? .title3.weight(.bold) : .subheadline.weight(.bold))
                    .multilineTextAlignment(.center)
                    .lineLimit(3)
                    .minimumScaleFactor(0.7)
            }
            .foregroundStyle(Palette.pine)
            .padding(10)
            .frame(width: width, height: height)
            .background(
                RoundedRectangle(cornerRadius: 20, style: .continuous)
                    .fill(active ? Palette.sage.opacity(0.92) : Color.white.opacity(0.88))
            )
            .overlay(
                RoundedRectangle(cornerRadius: 20, style: .continuous)
                    .strokeBorder(active ? Palette.moss : Palette.moss.opacity(0.55), lineWidth: active ? 3 : 2)
            )
            .shadow(color: Palette.pine.opacity(0.12), radius: 4, y: 2)
        }
        .buttonStyle(.plain)
        .accessibilityLabel("Speech bubble: \(text)")
        .accessibilityHint("Tap to hear this bubble")
    }
}

struct ComicBubbleTapHint: View {
    let storyID: String

    var body: some View {
        if ComicSentenceSpeaker.isEnabled(for: storyID) {
            Text("点上面白色对话框可以听 · Tap a speech bubble to hear it")
                .font(.caption.weight(.bold))
                .foregroundStyle(Palette.moss)
                .frame(maxWidth: .infinity, alignment: .leading)
                .padding(.horizontal, 4)
        }
    }
}
