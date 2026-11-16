import AVFoundation
import SwiftUI
import UIKit

/// 点插图对话框里的单词朗读（先试 E-A01）。不改休息/计时。
@MainActor
final class ComicSentenceSpeaker: NSObject, ObservableObject {
    static let shared = ComicSentenceSpeaker()

    @Published private(set) var speakingText: String?

    private let synth = AVSpeechSynthesizer()
    private var bridge: SentenceSpeechBridge?
    private var bubbleCache: [String: [CGRect]] = [:]

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

    func speakWord(_ raw: String) {
        let spoken = Self.speakable(raw)
        guard !spoken.isEmpty else { return }

        let player = BedtimeAudioPlayer.shared
        if player.isPlaying {
            player.togglePauseResume()
        }
        if synth.isSpeaking {
            synth.stopSpeaking(at: .immediate)
        }

        speakingText = raw
        let utterance = AVSpeechUtterance(string: spoken)
        utterance.voice = Self.bestEnglishVoice()
        utterance.rate = AVSpeechUtteranceDefaultSpeechRate * 0.86
        utterance.pitchMultiplier = 1.03
        utterance.preUtteranceDelay = 0.02
        utterance.postUtteranceDelay = 0.02
        try? AVAudioSession.sharedInstance().setCategory(.playback, mode: .spokenAudio, options: [.duckOthers])
        try? AVAudioSession.sharedInstance().setActive(true)
        synth.speak(utterance)
    }

    fileprivate func didFinish() {
        speakingText = nil
    }

    func bubbleFrames(for image: UIImage, cacheKey: String) -> [CGRect] {
        if let cached = bubbleCache[cacheKey], cached.count >= 2 {
            return Array(cached.prefix(2))
        }
        let found = Self.findTwoBubbles(in: image)
        if found.count >= 2 {
            bubbleCache[cacheKey] = found
            return found
        }
        // Fallback zones if detection misses (normalized later in view)
        return []
    }

    static func words(in phrase: String) -> [String] {
        phrase
            .split(whereSeparator: { $0.isWhitespace })
            .map(String.init)
            .filter { !$0.isEmpty }
    }

    static func speakable(_ raw: String) -> String {
        let trimmed = raw.trimmingCharacters(in: .whitespacesAndNewlines)
        let kept = trimmed.filter { $0.isLetter || $0.isNumber || $0 == "'" || $0 == "’" || $0 == "-" }
        return kept.isEmpty ? trimmed : String(kept)
    }

    private static func bestEnglishVoice() -> AVSpeechSynthesisVoice? {
        let voices = AVSpeechSynthesisVoice.speechVoices().filter { $0.language.hasPrefix("en") }
        return voices.first(where: { $0.quality == .enhanced && $0.language.hasPrefix("en-US") })
            ?? voices.first(where: { $0.language.hasPrefix("en-US") })
            ?? AVSpeechSynthesisVoice(language: "en-US")
            ?? AVSpeechSynthesisVoice(language: "en-GB")
    }

    /// Downscaled white-blob finder → up to two bubble rects in image-pixel space, left→right.
    private static func findTwoBubbles(in image: UIImage) -> [CGRect] {
        guard let cg = image.cgImage else { return [] }
        let fullW = cg.width
        let fullH = cg.height
        let maxSide = 320
        let scale = min(1.0, CGFloat(maxSide) / CGFloat(max(fullW, fullH)))
        let w = max(1, Int(CGFloat(fullW) * scale))
        let h = max(1, Int(CGFloat(fullH) * scale))
        let topH = Int(CGFloat(h) * 0.72)

        guard let ctx = CGContext(
            data: nil,
            width: w,
            height: h,
            bitsPerComponent: 8,
            bytesPerRow: w * 4,
            space: CGColorSpaceCreateDeviceRGB(),
            bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue
        ) else { return [] }

        ctx.interpolationQuality = .low
        ctx.draw(cg, in: CGRect(x: 0, y: 0, width: w, height: h))
        guard let data = ctx.data else { return [] }
        let ptr = data.bindMemory(to: UInt8.self, capacity: w * h * 4)

        func isWhite(_ x: Int, _ y: Int) -> Bool {
            let i = (y * w + x) * 4
            let r = Int(ptr[i]), g = Int(ptr[i + 1]), b = Int(ptr[i + 2])
            return r >= 245 && g >= 245 && b >= 245
        }

        var visited = [Bool](repeating: false, count: w * topH)
        var comps: [(CGRect, Int, CGFloat, CGFloat)] = []

        for y in 0..<topH {
            for x in 0..<w {
                let vi = y * w + x
                if visited[vi] { continue }
                if !isWhite(x, y) {
                    visited[vi] = true
                    continue
                }
                var q = [(x, y)]
                visited[vi] = true
                var minx = x, maxx = x, miny = y, maxy = y, count = 0
                var qi = 0
                while qi < q.count {
                    let (cx, cy) = q[qi]; qi += 1
                    count += 1
                    minx = min(minx, cx); maxx = max(maxx, cx)
                    miny = min(miny, cy); maxy = max(maxy, cy)
                    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                        let nx = cx + dx, ny = cy + dy
                        if nx < 0 || nx >= w || ny < 0 || ny >= topH { continue }
                        let ni = ny * w + nx
                        if visited[ni] { continue }
                        if isWhite(nx, ny) {
                            visited[ni] = true
                            q.append((nx, ny))
                        } else {
                            visited[ni] = true
                        }
                    }
                }
                let bw = maxx - minx, bh = maxy - miny
                if count < Int(Double(w * h) * 0.006) { continue }
                if bw < Int(Double(w) * 0.10) || bh < Int(Double(h) * 0.07) { continue }
                if bw > Int(Double(w) * 0.58) || bh > Int(Double(h) * 0.48) { continue }
                let area = max(1, bw * bh)
                let fill = CGFloat(count) / CGFloat(area)
                if fill < 0.35 { continue }
                let aspect = CGFloat(bw) / CGFloat(max(1, bh))
                if aspect > 3.5 || aspect < 0.5 { continue }
                let rect = CGRect(x: minx, y: miny, width: bw, height: bh)
                let cy = CGFloat(miny + maxy) / 2
                comps.append((rect, count, fill, cy))
            }
        }

        guard comps.count >= 2 else { return [] }
        comps.sort { a, b in
            let upperA = 1.2 - (a.3 / CGFloat(h))
            let upperB = 1.2 - (b.3 / CGFloat(h))
            return CGFloat(a.1) * a.2 * max(0.3, upperA) > CGFloat(b.1) * b.2 * max(0.3, upperB)
        }
        let first = comps[0]
        let fcx = first.0.midX
        var second: (CGRect, Int, CGFloat, CGFloat)?
        for c in comps.dropFirst() {
            if abs(c.0.midX - fcx) < CGFloat(w) * 0.14 { continue }
            let inter = first.0.intersection(c.0)
            if !inter.isNull, inter.width > 0, inter.height > 0 {
                let area = c.0.width * c.0.height
                if area > 0, (inter.width * inter.height) / area > 0.4 { continue }
            }
            second = c
            break
        }
        guard let second else { return [] }
        let inv = 1.0 / scale
        let pair = [first.0, second.0]
            .sorted { $0.minX < $1.minX }
            .map { CGRect(x: $0.minX * inv, y: $0.minY * inv, width: $0.width * inv, height: $0.height * inv) }
        return pair
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

// MARK: - Bubble text catalog (trial)

enum ComicBubbleWordsCatalog {
    private static let data: [String: [[String: String]]] = {
        guard let url = Bundle.main.url(forResource: "ComicBubbleWords.en", withExtension: "json"),
              let raw = try? Data(contentsOf: url),
              let obj = try? JSONSerialization.jsonObject(with: raw) as? [String: [[String: Any]]]
        else { return [:] }
        var out: [String: [[String: String]]] = [:]
        for (sid, panels) in obj {
            out[sid] = panels.map { panel in
                [
                    "left": panel["left"] as? String ?? "",
                    "right": panel["right"] as? String ?? "",
                ]
            }
        }
        return out
    }()

    static func bubbles(storyID: String, pageIndex: Int) -> (left: String, right: String)? {
        guard let panels = data[storyID], panels.indices.contains(pageIndex) else { return nil }
        let p = panels[pageIndex]
        return (p["left"] ?? "", p["right"] ?? "")
    }
}

/// 叠在插图对话框上：每个单词可点朗读。
struct ComicBubbleWordOverlay: View {
    let storyID: String
    let pageIndex: Int
    let imageURL: URL

    @ObservedObject private var speaker = ComicSentenceSpeaker.shared
    @State private var frames: [CGRect] = []
    @State private var imageSize: CGSize = .zero

    private var phrases: (left: String, right: String)? {
        ComicBubbleWordsCatalog.bubbles(storyID: storyID, pageIndex: pageIndex)
    }

    var body: some View {
        GeometryReader { geo in
            let layout = fittedImageRect(container: geo.size, image: imageSize)
            ZStack(alignment: .topLeading) {
                Color.clear
                if let phrases {
                    let bubbleRects = resolvedBubbleRects(in: layout)
                    if bubbleRects.count >= 2 {
                        wordBubble(phrases.left, in: bubbleRects[0])
                        wordBubble(phrases.right, in: bubbleRects[1])
                    } else {
                        // 检测失败时仍盖在上方左右，保证能点
                        wordBubble(phrases.left, in: fallbackLeft(layout))
                        wordBubble(phrases.right, in: fallbackRight(layout))
                    }
                }
            }
            .frame(width: geo.size.width, height: geo.size.height)
            .onAppear { refreshFrames() }
            .onChange(of: imageURL) { _, _ in refreshFrames() }
            .onChange(of: pageIndex) { _, _ in refreshFrames() }
        }
        .allowsHitTesting(true)
    }

    private func wordBubble(_ phrase: String, in rect: CGRect) -> some View {
        let words = ComicSentenceSpeaker.words(in: phrase)
        return VStack(alignment: .leading, spacing: 4) {
            FlowWordRow(words: words, speaking: speaker.speakingText) { word in
                speaker.speakWord(word)
            }
        }
        .padding(.horizontal, 10)
        .padding(.vertical, 8)
        .frame(width: max(44, rect.width), height: max(36, rect.height), alignment: .center)
        .background(
            RoundedRectangle(cornerRadius: 18, style: .continuous)
                .fill(Color.white.opacity(0.94))
        )
        .overlay(
            RoundedRectangle(cornerRadius: 18, style: .continuous)
                .strokeBorder(Palette.moss.opacity(0.35), lineWidth: 1.5)
        )
        .position(x: rect.midX, y: rect.midY)
        .accessibilityElement(children: .contain)
    }

    private func refreshFrames() {
        guard let ui = ComicImageCache.image(at: imageURL) else {
            frames = []
            imageSize = .zero
            return
        }
        imageSize = ui.size
        frames = speaker.bubbleFrames(for: ui, cacheKey: imageURL.path)
    }

    private func fittedImageRect(container: CGSize, image: CGSize) -> CGRect {
        guard image.width > 0, image.height > 0, container.width > 0, container.height > 0 else {
            return CGRect(origin: .zero, size: container)
        }
        let scale = min(container.width / image.width, container.height / image.height)
        let w = image.width * scale
        let h = image.height * scale
        return CGRect(
            x: (container.width - w) / 2,
            y: (container.height - h) / 2,
            width: w,
            height: h
        )
    }

    private func resolvedBubbleRects(in layout: CGRect) -> [CGRect] {
        guard imageSize.width > 0, !frames.isEmpty else { return [] }
        let sx = layout.width / imageSize.width
        let sy = layout.height / imageSize.height
        return frames.map { r in
            CGRect(
                x: layout.minX + r.minX * sx,
                y: layout.minY + r.minY * sy,
                width: r.width * sx,
                height: r.height * sy
            ).insetBy(dx: 2, dy: 2)
        }
    }

    private func fallbackLeft(_ layout: CGRect) -> CGRect {
        CGRect(
            x: layout.minX + layout.width * 0.04,
            y: layout.minY + layout.height * 0.03,
            width: layout.width * 0.42,
            height: layout.height * 0.26
        )
    }

    private func fallbackRight(_ layout: CGRect) -> CGRect {
        CGRect(
            x: layout.minX + layout.width * 0.54,
            y: layout.minY + layout.height * 0.03,
            width: layout.width * 0.42,
            height: layout.height * 0.26
        )
    }
}

private struct FlowWordRow: View {
    let words: [String]
    let speaking: String?
    let onTap: (String) -> Void

    var body: some View {
        FlexibleWordWrap(words: words, spacing: 6, lineSpacing: 4) { word in
            Button {
                onTap(word)
            } label: {
                Text(word)
                    .font(HavenLayout.isPad ? .title3.weight(.bold) : .body.weight(.bold))
                    .foregroundStyle(Palette.pine)
                    .padding(.horizontal, 6)
                    .padding(.vertical, 3)
                    .background(
                        Capsule()
                            .fill(speaking == word ? Palette.sage.opacity(0.85) : Color.white.opacity(0.01))
                    )
                    .overlay(
                        Capsule()
                            .strokeBorder(
                                speaking == word ? Palette.moss : Palette.pine.opacity(0.2),
                                lineWidth: speaking == word ? 2 : 1
                            )
                    )
            }
            .buttonStyle(.plain)
            .accessibilityLabel("Word \(ComicSentenceSpeaker.speakable(word))")
            .accessibilityHint("Tap to hear")
        }
    }
}

/// Simple wrap layout for tappable words.
private struct FlexibleWordWrap<Item: View>: View {
    let words: [String]
    var spacing: CGFloat = 6
    var lineSpacing: CGFloat = 4
    @ViewBuilder var item: (String) -> Item

    var body: some View {
        // Adaptive grid keeps taps large enough for kids
        LazyVGrid(
            columns: [GridItem(.adaptive(minimum: 52), spacing: spacing, alignment: .leading)],
            alignment: .leading,
            spacing: lineSpacing
        ) {
            ForEach(Array(words.enumerated()), id: \.offset) { _, word in
                item(word)
            }
        }
    }
}

/// 提示条：告诉家长点气泡单词。
struct ComicBubbleTapHint: View {
    let storyID: String

    var body: some View {
        if ComicSentenceSpeaker.isEnabled(for: storyID) {
            Text("点气泡里的单词可以听 · Tap a word in the bubble")
                .font(.caption.weight(.semibold))
                .foregroundStyle(Palette.moss)
                .frame(maxWidth: .infinity, alignment: .leading)
                .padding(.horizontal, 4)
        }
    }
}
