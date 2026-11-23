import re


def split_into_chunks(text: str, max_words: int = 50) -> list[str]:
    """Split text into pieces of at most max_words words."""
    words = text.split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]


def tokenize(text: str) -> set[str]:
    """Lowercase the text and return its set of words."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def score(query: str, chunk: str) -> int:
    """Count how many words the query and the chunk share."""
    return len(tokenize(query) & tokenize(chunk))


def find_best_chunks(query: str, chunks: list[str], top_k: int = 3) -> list[str]:
    """Return the top_k chunks that best match the query, best first."""
    scored = [(score(query, chunk), chunk) for chunk in chunks]
    scored = [item for item in scored if item[0] > 0]
    scored.sort(key=lambda item: item[0], reverse=True)
    return [chunk for _, chunk in scored[:top_k]]