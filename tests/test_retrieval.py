from app.retrieval import find_best_chunks, split_into_chunks


def test_split_into_chunks_respects_max_words():
    text = " ".join(str(i) for i in range(120))
    chunks = split_into_chunks(text, max_words=50)
    assert len(chunks) == 3
    assert all(len(chunk.split()) <= 50 for chunk in chunks)


def test_find_best_chunks_returns_most_relevant_first():
    chunks = [
        "Cats sleep a lot.",
        "Python is a programming language.",
        "The sea is blue.",
    ]
    result = find_best_chunks("what is python", chunks, top_k=1)
    assert result == ["Python is a programming language."]