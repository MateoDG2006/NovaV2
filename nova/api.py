from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

from .llm import Message, Model
from .settings import OLLAMA_BASE_URL, OLLAMA_MODEL
from .views import chat_stream_view, chat_view

app = FastAPI()

model = Model(
    name=OLLAMA_MODEL,
    version="1.0",
    model_base_url=OLLAMA_BASE_URL
)

@app.get("/")
async def home(request: Request):
    # view helper is async, so await it
    return await chat_view(request, context={})

@app.get("/chat")
async def chat_page(request: Request):
    return await chat_view(request, context={})


@app.post("/chat")
async def chat_endpoint(message: Message):
    # the body is parsed as a Message model
    response = model.chat(message)
    return response


@app.get("/chat-stream")
async def chat_stream_page(request: Request):
    return await chat_stream_view(request, context={})

@app.post("/chat-stream")
async def chat_stream_endpoint(message: str):
    return model.chat_stream(Message(content=message))