# 🧠 Human-like Social Media Reply Generator

This project generates short, natural replies to social media posts using a sentiment-aware LLM workflow.

> 🚀 Built with FastAPI, Hugging Face Transformers, and CSV storage (MongoDB-ready)

---

## 📌 Features

✅ Natural Language Generation with tone awareness  
✅ Supports LinkedIn, Instagram, Twitter post contexts  
✅ Smart prompt design to avoid repetition and generic replies  
✅ API returns short, human-like responses  
✅ Saves all replies to a CSV file (`generated_replies.csv`)  
✅ Clean RESTful API with Swagger docs

---

## 🧠 NLG Strategy

This system uses:
- **Sentiment detection** (positive, negative, neutral)
- **Prompt chaining** to adapt tone & platform context
- Hugging Face's `flan-t5-base` for lightweight reply generation



---

## ⚙️ How to Run

### 1. Clone the repo
```bash
git clone https://github.com/Nishra-Parikh/human_reply_generator.git
cd human-reply-generator

### 2.Create virtual environment
python -m venv venv
venv\Scripts\activate    # Windows


###3.Install dependencies
pip install -r requirements.txt


###4.Run the API
uvicorn app.main:app --reload

#Go to local host 

## use the /reply endpoint with: THis is the request structer for testing
{
  "platform": "Instagram",
  "post_text": "Feeling excited to start my new job!"
}


# Response:
{
  "generated_reply": "That's wonderful! Grateful teams are the best."
}


## stoarge :
stoarge will be in genrated_replies.csv as the mongodb was not suporting