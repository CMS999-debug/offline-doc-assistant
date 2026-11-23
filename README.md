# Offline Document Assistant

A small API that lets you add documents and ask questions about them. It finds the passages that best match your question. The long-term goal is an assistant that runs fully offline, with no internet connection.

**Status:** work in progress (started November 2026). Built with AI assistance, with every change reviewed and tested by me.

## What works today
- `POST /documents`: add text, which is split into chunks
- `POST /ask`: returns the passages that best match a question (keyword matching)
- `GET /health`: service health check
- Automated tests with pytest

## Run it
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Then open `/docs` for the interactive API page.

## Run the tests
```
python -m pytest
```

## Project structure
```
app/main.py         API endpoints
app/retrieval.py    chunking and keyword search
tests/              automated tests
```

## Known limitations
- Matching is by shared words only, so it misses synonyms and meaning.
- Documents are stored in memory and are lost when the server restarts.
- It does not generate answers yet, only returns matching passages.

## Roadmap
- [ ] Evaluation script: a set of test questions with a measured accuracy score
- [ ] Better retrieval using embeddings, compared against the baseline
- [ ] Local language model to generate answers offline
- [ ] Docker and GitHub Actions CI

## What I'm learning
Python, FastAPI, testing, Git, and how retrieval-based assistants work.
