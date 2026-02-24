from fastapi import FastAPI, Body
from ollama import Client

app = FastAPI()
client = Client(
    host = "http://localhost:11434"
)

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/contact_us")
def contact_us():
    return {"email": "mhamza7197@gmail.com"}

@app.post("/chat")
def chat(
    message: str = Body(..., description="the massegae")
):
    response = client.chat(model="gemma3:1b", messages=[
        { "role": "user", "content":message}
    ])

    return { "response": response.message.content}