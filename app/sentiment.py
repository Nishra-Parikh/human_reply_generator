from transformers import pipeline

# Load the sentiment classifier once
classifier = pipeline("sentiment-analysis")

def detect_sentiment(text: str) -> str:
    try:
        result = classifier(text)[0]
        label = result["label"].lower()  # 'positive', 'negative'
        score = result["score"]

        if score < 0.6:
            return "neutral"
        return label
    except Exception:
        return "neutral"
