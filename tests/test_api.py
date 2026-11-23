from fastapi.testclient import TestClient

from app.main import app, documents

client = TestClient(app)


def setup_function():
    documents.clear()


def test_ask_returns_relevant_passage():
    client.post(
        "/documents",
        json={"text": "Python is a programming language. The sea is blue."},
    )
    response = client.post("/ask", json={"question": "what is python"})
    assert response.status_code == 200
    assert "Python is a programming language" in response.json()["matches"][0]


def test_ask_with_no_documents_returns_404():
    response = client.post("/ask", json={"question": "anything"})
    assert response.status_code == 404