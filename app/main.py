from fastapi import FastAPI, HTTPException
from app.models import PostRequest, PostResponse
from app.generator import generate_reply
from app.db import save_to_csv

app = FastAPI(title="Human-like Social Media Reply Generator")

@app.post("/reply", response_model=PostResponse)
async def get_reply(request: PostRequest):
    try:
        reply = await generate_reply(request.platform, request.post_text)
        await save_to_csv(request.platform, request.post_text, reply)
        return {"generated_reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
