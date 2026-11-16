import AVFoundation
import SwiftUI

/// 点插图对话框朗读。有气泡文案的 12 页绘本都显示角上喇叭。不改休息/计时。
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
        ComicBubbleWordsCatalog.hasBubbles(storyID)
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

/// 从 Bundle 的 ComicBubbleWords.en.json 读左右气泡；读不到时用内置 E-A01 兜底。
enum ComicBubbleWordsCatalog {
    private struct Page: Decodable {
        let i: Int
        let left: String
        let right: String
    }

    private static let pagesByStory: [String: [(String, String)]] = {
        if let url = Bundle.main.url(forResource: "ComicBubbleWords.en", withExtension: "json"),
           let data = try? Data(contentsOf: url),
           let decoded = try? JSONDecoder().decode([String: [Page]].self, from: data)
        {
            var map: [String: [(String, String)]] = [:]
            for (id, pages) in decoded {
                let ordered = pages.sorted { $0.i < $1.i }.map { ($0.left, $0.right) }
                if !ordered.isEmpty {
                    map[id] = ordered
                }
            }
            if !map.isEmpty { return map }
        }
        return ["E-A01": fallbackBirds]
    }()

    private static let fallbackBirds: [(String, String)] = [
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

    static func hasBubbles(_ storyID: String) -> Bool {
        pagesByStory[storyID] != nil
    }

    static func bubbles(storyID: String, pageIndex: Int) -> (left: String, right: String)? {
        guard let pages = pagesByStory[storyID], pages.indices.contains(pageIndex) else { return nil }
        let p = pages[pageIndex]
        return (p.0, p.1)
    }
}

/// 只在插图左上角 / 右上角放小喇叭；点一下读对应气泡整句。
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
                    VStack {
                        HStack {
                            cornerSpeaker(phrases.left)
                            Spacer(minLength: 0)
                        }
                        Spacer(minLength: 0)
                    }
                    .padding(pad)

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
