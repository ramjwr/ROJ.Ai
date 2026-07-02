from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key="PUT_YOUR_API_KEY_HERE")


@app.get("/")
def home():
    return {"message": "AI with memory is running"}

@app.get("/ask")
def ask(q: str):

    # حفظ رسالة المستخدم
    save("user", q)

    # تحميل آخر 10 رسائل من قاعدة البيانات
    context = load_last(10)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI that remembers previous conversations."
            },
            *context
        ]
    )

    answer = response.choices[0].message.content

    # حفظ رد الذكاء الاصطناعي
    save("assistant", answer)

    return {"answer": answer}