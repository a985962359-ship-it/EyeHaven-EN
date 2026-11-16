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

/// 只在左右对话气泡角上放小喇叭；不盖白框、不盖文字。
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
                // 热区对齐常见气泡位置：上半左右；视觉只有角落小喇叭
                let zoneW = w * 0.42
                let zoneH = max(64, h * 0.30)
                let topPad = h * 0.04
                let sidePad = w * 0.04

                ZStack(alignment: .topLeading) {
                    speakerHotspot(
                        text: phrases.left,
                        width: zoneW,
                        height: zoneH,
                        iconCorner: .topTrailing
                    )
                    .offset(x: sidePad, y: topPad)

                    speakerHotspot(
                        text: phrases.right,
                        width: zoneW,
                        height: zoneH,
                        iconCorner: .topLeading
                    )
                    .offset(x: w - sidePad - zoneW, y: topPad)
                }
                .frame(width: w, height: h, alignment: .topLeading)
            }
            .allowsHitTesting(true)
        }
    }

    private enum IconCorner {
        case topLeading, topTrailing
    }

    private func speakerHotspot(
        text: String,
        width: CGFloat,
        height: CGFloat,
        iconCorner: IconCorner
    ) -> some View {
        let active = speaker.speakingText == text
        return Button {
            speaker.speakPhrase(text)
        } label: {
            ZStack(alignment: iconCorner == .topLeading ? .topLeading : .topTrailing) {
                Color.clear
                    .frame(width: width, height: height)
                    .contentShape(Rectangle())

                Image(systemName: active ? "speaker.wave.2.fill" : "speaker.wave.2.fill")
                    .font(.system(size: HavenLayout.isPad ? 18 : 15, weight: .bold))
                    .foregroundStyle(active ? Palette.moss : Palette.pine.opacity(0.85))
                    .padding(6)
                    .background(
                        Circle()
                            .fill(Color.white.opacity(active ? 0.92 : 0.78))
                    )
                    .shadow(color: Palette.pine.opacity(0.18), radius: 2, y: 1)
                    .padding(8)
                    .scaleEffect(active ? 1.12 : 1.0)
                    .animation(.easeInOut(duration: 0.15), value: active)
            }
        }
        .buttonStyle(.plain)
        .accessibilityLabel("Hear: \(text)")
        .accessibilityHint("Tap the speaker in the speech bubble")
    }
}

struct ComicBubbleTapHint: View {
    let storyID: String

    var body: some View {
        if ComicSentenceSpeaker.isEnabled(for: storyID) {
            Text("点气泡里小喇叭可以听 · Tap the speaker in a bubble")
                .font(.caption.weight(.bold))
                .foregroundStyle(Palette.moss)
                .frame(maxWidth: .infinity, alignment: .leading)
                .padding(.horizontal, 4)
        }
    }
}
