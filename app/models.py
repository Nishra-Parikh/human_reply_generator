from pydantic import BaseModel
from typing import Literal

class PostRequest(BaseModel):
    platform: Literal["LinkedIn", "Instagram", "Twitter"]
    post_text: str

class PostResponse(BaseModel):
    generated_reply: str
