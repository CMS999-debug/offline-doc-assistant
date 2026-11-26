from app.retrieval import find_best_chunks

FACTS = [
    "Python is a programming language created by Guido van Rossum.",
    "The River Cam flows through the centre of Cambridge.",
    "Photosynthesis lets plants turn sunlight into chemical energy.",
    "The Great Wall of China was built over many centuries to protect against invasions.",
    "Mount Everest is the highest mountain above sea level.",
    "Water boils at 100 degrees Celsius at sea level.",
    "The heart pumps blood around the human body.",
    "Git is a version control system used to track changes in code.",
    "Neural networks are made of layers of connected nodes.",
    "A binary search repeatedly halves a sorted list to find a value.",
]

# (question, index of the fact that should come back first)
QUESTIONS = [
    ("Who created Python?", 0),
    ("Which river flows through Cambridge?", 1),
    ("How do green organisms use light to make fuel?", 2),
    ("Why was the Great Wall built?", 3),
    ("What is the tallest mountain?", 4),
    ("At what temperature does water boil?", 5),
    ("What organ moves blood around the body?", 6),
    ("Which software helps developers collaborate on source files?", 7),
    ("How do deep learning models work?", 8),
    ("How can I quickly find a value in sorted data?", 9),
]


def evaluate() -> float:
    correct = 0
    for question, expected_index in QUESTIONS:
        results = find_best_chunks(question, FACTS, top_k=1)
        hit = results == [FACTS[expected_index]]
        correct += hit
        print(f"{'PASS' if hit else 'FAIL'}  {question}")
    accuracy = correct / len(QUESTIONS)
    print(f"\nTop-1 accuracy: {accuracy:.0%} ({correct}/{len(QUESTIONS)})")
    return accuracy


if __name__ == "__main__":
    evaluate()