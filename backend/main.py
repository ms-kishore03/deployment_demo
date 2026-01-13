from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/message")
def message():
    return {
        "message": "Hello from backend",
        "time": datetime.utcnow().isoformat()
    }
