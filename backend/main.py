from fastapi import FastAPI
from api.chat import router as chat_router

app = FastAPI(
    title="RojAI",
    version="0.1"
)

app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "project": "RojAI",
        "status": "Running"
    }