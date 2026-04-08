from fastapi import FastAPI
from textblob import TextBlob

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running"}

@app.post("/analyze")
def analyze(text: str):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    return {
        "input_text": text,
        "sentiment": sentiment,
        "polarity_score": polarity
    }