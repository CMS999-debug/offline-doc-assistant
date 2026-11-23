from fastapi import FastAPI

app = FastAPI(title="Offline Document Assistant")


@app.get("/health")
def health():
    return {"status": "ok"}