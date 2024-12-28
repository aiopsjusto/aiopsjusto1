from transformers import pipeline
from fastapi import FastAPI, Request

app = FastAPI()
sentiment_analyzer = pipeline("sentiment-analysis")

@app.post("/analyze")
async def analyze_sentiment(request: Request):
    data = await request.json()
    sentiment = sentiment_analyzer(data["text"])
    return {"sentiment": sentiment}