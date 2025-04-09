from pydantic import BaseModel
from fastapi import APIRouter
from app.services.ai_service import chat_with_history
from typing import List, Optional

class Message(BaseModel):
    role: str
    content: str

class ChatQuery(BaseModel):
    prompt: Message
    previous_messages: Optional[List[Message]] = None

class ChatResponse(BaseModel):
    response: str

router = APIRouter()

@router.post("/")
async def query_chat(chat_query: ChatQuery):
    prompt = chat_query.prompt
    print(f"Received query: {prompt}")
    response = chat_with_history(prompt, previous_messages=chat_query.previous_messages)
    return {"response": response}