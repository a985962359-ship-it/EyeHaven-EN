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
                let pad: CGFloat = HavenLayout.isPad ? 10 : 8
                ZStack {
                    // 左上角：左气泡
                    VStack {
                        HStack {
                            cornerSpeaker(phrases.left)
                            Spacer(minLength: 0)
                        }
                        Spacer(minLength: 0)
                    }
                    .padding(pad)

                    // 右上角：右气泡
                    VStack {
                        HStack {
                            Spacer(minLength: 0)
                            cornerSpeaker(phrases.right)
                        }
                        Spacer(minLength: 0)
                    }
                    .padding(pad)
                }
                .frame(width: geo.size.width, height: geo.size.height)
            }
            .allowsHitTesting(true)
        }
    }

    private func cornerSpeaker(_ text: String) -> some View {
        let active = speaker.speakingText == text
        let size: CGFloat = HavenLayout.isPad ? 44 : 38
        return Button {
            speaker.speakPhrase(text)
        } label: {
            Image(systemName: "speaker.wave.2.fill")
                .font(.system(size: HavenLayout.isPad ? 18 : 15, weight: .bold))
                .foregroundStyle(active ? Palette.moss : Palette.pine.opacity(0.9))
                .frame(width: size, height: size)
                .background(
                    Circle()
                        .fill(Color.white.opacity(active ? 0.95 : 0.82))
                )
                .shadow(color: Palette.pine.opacity(0.2), radius: 2, y: 1)
                .scaleEffect(active ? 1.1 : 1.0)
                .animation(.easeInOut(duration: 0.15), value: active)
                .contentShape(Circle())
        }
        .buttonStyle(.plain)
        .accessibilityLabel("Hear: \(text)")
        .accessibilityHint("Tap the speaker")
    }
}

struct ComicBubbleTapHint: View {
    let storyID: String

    var body: some View {
        if ComicSentenceSpeaker.isEnabled(for: storyID) {
            Text("点左上角/右上角小喇叭可以听 · Tap the corner speakers")
                .font(.caption.weight(.bold))
                .foregroundStyle(Palette.moss)
                .frame(maxWidth: .infinity, alignment: .leading)
                .padding(.horizontal, 4)
        }
    }
}
