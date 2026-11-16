import AVFoundation
import SwiftUI

/// 插图页「点整句朗读」：试用于学单词。不改休息/计时。
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

    /// Trial gate: only first remodeled Birds story for now.
    static func isEnabled(for storyID: String) -> Bool {
        storyID == "E-A01"
    }

    /// One tappable line per comic page (blank-line paragraphs).
    static func pageLines(for story: BedtimeStory) -> [String] {
        story.text
            .components(separatedBy: "\n\n")
            .map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }
            .filter { !$0.isEmpty }
    }

    func speak(_ text: String) {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty else { return }

        // Pause story audio so the tapped sentence is clear.
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
        utterance.preUtteranceDelay = 0.05
        utterance.postUtteranceDelay = 0.05
        try? AVAudioSession.sharedInstance().setCategory(.playback, mode: .spokenAudio, options: [.duckOthers])
        try? AVAudioSession.sharedInstance().setActive(true)
        synth.speak(utterance)
    }

    func stop() {
        if synth.isSpeaking {
            synth.stopSpeaking(at: .immediate)
        }
        speakingText = nil
    }

    fileprivate func didFinish() {
        speakingText = nil
    }

    private static func bestEnglishVoice() -> AVSpeechSynthesisVoice? {
        let voices = AVSpeechSynthesisVoice.speechVoices().filter {
            $0.language.hasPrefix("en")
        }
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

/// 插图下方：本页整句，点击朗读。
struct ComicPageSentenceBar: View {
    let story: BedtimeStory
    let pageIndex: Int

    @ObservedObject private var speaker = ComicSentenceSpeaker.shared

    private var lines: [String] {
        ComicSentenceSpeaker.pageLines(for: story)
    }

    private var pageLine: String? {
        guard lines.indices.contains(pageIndex) else { return nil }
        return lines[pageIndex]
    }

    var body: some View {
        if ComicSentenceSpeaker.isEnabled(for: story.id), let pageLine {
            VStack(alignment: .leading, spacing: 8) {
                Text("Tap the sentence to hear it")
                    .font(.caption2.weight(.semibold))
                    .foregroundStyle(Palette.pine.opacity(0.65))

                Button {
                    speaker.speak(pageLine)
                } label: {
                    HStack(alignment: .top, spacing: 10) {
                        Image(systemName: speaker.speakingText == pageLine ? "speaker.wave.2.fill" : "speaker.wave.2")
                            .font(.body.weight(.semibold))
                            .foregroundStyle(Palette.moss)
                            .padding(.top, 2)
                        Text(pageLine)
                            .font(HavenLayout.isPad ? .title3.weight(.semibold) : .body.weight(.semibold))
                            .foregroundStyle(Palette.pine)
                            .multilineTextAlignment(.leading)
                            .frame(maxWidth: .infinity, alignment: .leading)
                    }
                    .padding(12)
                    .background(
                        RoundedRectangle(cornerRadius: 14, style: .continuous)
                            .fill(speaker.speakingText == pageLine ? Palette.sage.opacity(0.55) : Palette.mist)
                    )
                    .overlay(
                        RoundedRectangle(cornerRadius: 14, style: .continuous)
                            .strokeBorder(Palette.moss.opacity(0.35), lineWidth: 1)
                    )
                }
                .buttonStyle(.plain)
                .accessibilityLabel("Tap to hear: \(pageLine)")
            }
            .frame(maxWidth: .infinity, alignment: .leading)
        }
    }
}
