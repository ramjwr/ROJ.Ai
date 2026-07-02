from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
def chat(message: dict):
    user_message = message.get("message", "")

    return {
        "reply": f"You said: {user_message}"
    }