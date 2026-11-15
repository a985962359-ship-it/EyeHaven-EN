import Foundation

struct RestStory: Identifiable, Equatable {
    var id: String
    var title: String
    var text: String

    /// Rough listen length for English (~130 words per minute at slow rest pace).
    var minutes: Int {
        let words = text.split { $0.isWhitespace || $0.isNewline }.count
        return max(1, words / 130)
    }

    var paragraphs: [String] {
        text.components(separatedBy: "\n")
            .map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }
            .filter { !$0.isEmpty }
    }
}

enum RestStoryLibrary {
    static let all: [RestStory] = [
        .init(id: "turtle-rabbit", title: "The Tortoise and the Hare", text: turtleRabbit),
        .init(id: "crow-water", title: "The Crow and the Pitcher", text: crowWater),
        .init(id: "lion-mouse", title: "The Lion and the Mouse", text: lionMouse),
        .init(id: "boy-wolf", title: "The Boy Who Cried Wolf", text: boyWolf),
        .init(id: "north-wind", title: "The North Wind and the Sun", text: northWind),
        .init(id: "fox-crow", title: "The Fox and the Crow", text: foxCrow),
        .init(id: "city-mouse", title: "The Town Mouse and the Country Mouse", text: cityMouse),
        .init(id: "ant-hopper", title: "The Ant and the Grasshopper", text: antHopper),
        .init(id: "three-pigs", title: "The Three Little Pigs", text: threePigs),
        .init(id: "ugly-duck", title: "The Ugly Duckling", text: uglyDuck),
        .init(id: "new-clothes", title: "The Emperor’s New Clothes", text: newClothes),
        .init(id: "red-hood", title: "Little Red Riding Hood", text: redHood),
        .init(id: "goldilocks", title: "Goldilocks and the Three Bears", text: goldilocks),
        .init(id: "lost-sheep", title: "Mend the Pen", text: lostSheep),
        .init(id: "well-frog", title: "The Frog in the Well", text: wellFrog),
    ]

    static func next(after id: String?) -> RestStory {
        guard let id, let index = all.firstIndex(where: { $0.id == id }) else {
            return all[0]
        }
        return all[(index + 1) % all.count]
    }

    static func story(id: String) -> RestStory? {
        all.first { $0.id == id }
    }
}

private let turtleRabbit = """
A speedy hare laughed at a slow tortoise. “Race me,” said the tortoise. The hare raced ahead, then napped in soft grass. The tortoise kept one careful step after another. When the hare woke, the tortoise was already touching the finish stone. Fast is useful — but finishing matters more. Resting is like that too: stay quiet until you’re done.
"""

private let crowWater = """
A thirsty crow found a pitcher with only a little water at the bottom. He could not reach it. He dropped pebble after pebble into the pitcher. The water rose. At last he could drink. Small steady tries can solve a hard problem.
"""

private let lionMouse = """
A lion caught a tiny mouse. The mouse begged to be free and promised to help someday. The lion laughed and let him go. Later the lion was caught in a hunter’s net. The mouse chewed the ropes until the lion walked free. Kindness can come back when you need it.
"""

private let boyWolf = """
A shepherd boy shouted “Wolf!” when there was no wolf, just to watch people run. They came, then went home angry. When a real wolf came, the boy shouted again. Nobody believed him. The sheep were lost. Truth keeps friends ready to help.
"""

private let northWind = """
The North Wind and the Sun argued about who was stronger. They tried to make a traveler remove his coat. The Wind blew hard; the man held the coat tighter. The Sun shone gently warm; the man smiled and took the coat off. Gentle warmth can win where force fails.
"""

private let foxCrow = """
A crow held cheese in her beak. A fox praised her voice until she opened her beak to sing. The cheese fell. The fox ate it and said flattery is a cheap trick. Be careful with sweet words that want your prize.
"""

private let cityMouse = """
A country mouse visited a town mouse. The town food looked rich, but cats and noise made every bite scary. The country mouse went home to simple quiet meals. Peace can taste better than fancy fear.
"""

private let antHopper = """
All summer the ant stored food. The grasshopper sang and danced. When winter came, the grasshopper was cold and hungry. The ant shared a little, and the grasshopper learned to prepare. Fun is fine — and planning keeps you safe.
"""

private let threePigs = """
Three little pigs built houses of straw, sticks, and bricks. A wolf blew down the first two. The brick house stood. The pigs stayed safe inside. Strong work takes longer, but it protects you when trouble comes.
"""

private let uglyDuck = """
A duckling looked different and felt left out. He grew through cold seasons until he saw his reflection: a swan. He belonged with the swans all along. Growing can feel lonely before it feels right.
"""

private let newClothes = """
Two tricksters told an emperor that only clever people could see their magic cloth. Afraid of looking foolish, everyone praised the empty clothes. A child said the truth: the emperor had nothing on. Honest words help more than polite lies.
"""

private let redHood = """
Little Red Riding Hood carried food to Grandma. A wolf tricked her and reached the cottage first. A woodcutter helped, and Grandma was safe again. Stay on the path, and don’t tell strangers where you’re going.
"""

private let goldilocks = """
Goldilocks found a cottage with three bowls, three chairs, and three beds. She tried each one and fell asleep in the softest bed. The three bears came home and found her. She ran away and learned: other people’s things are not yours to take.
"""

private let lostSheep = """
A farmer lost sheep when the pen broke. Neighbors said fixing it was too late. He mended the pen anyway. Later storms came, and the flock stayed safe. Fixing a problem early still protects tomorrow.
"""

private let wellFrog = """
A frog lived in a well and thought the sky was only as wide as the well mouth. A turtle from the sea told him about oceans. The frog climbed out and saw a bigger world. Leave the well of old ideas when someone shows you more.
"""
