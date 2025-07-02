from transformers import pipeline
from app.sentiment import detect_sentiment

# Load Hugging Face model for generation
generator = pipeline("text2text-generation", model="google/flan-t5-base")

async def generate_reply(platform: str, post_text: str) -> str:
    sentiment = detect_sentiment(post_text)

    # Chained prompt strategy
    prompt = (
        f"You are replying to a {sentiment} {platform} post:\n"
        f"\"{post_text}\"\n\n"
        f"Write a short, human-like reply. Be kind and avoid repeating the post. "
        f"Keep the tone {sentiment} and natural."
    )

    try:
        response = generator(prompt, max_length=60, do_sample=True, temperature=0.9)
        raw_reply = response[0]["generated_text"].strip()
    except Exception:
        raw_reply = "Thanks for sharing your thoughts."

    # Clean fallback if reply is empty
    if not raw_reply or len(raw_reply) < 5:
        raw_reply = "Wishing you well on your journey!"

    return raw_reply
