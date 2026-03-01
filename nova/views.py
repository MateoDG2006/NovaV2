from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="nova/templates")


async def chat_view(request: Request, context: dict):
    data = {"request": request, **context}
    return templates.TemplateResponse("chat.html", data)

async def chat_stream_view(request: Request, context: dict):
    data = {"request": request, **context}
    return templates.TemplateResponse("chat_stream.html", data)
