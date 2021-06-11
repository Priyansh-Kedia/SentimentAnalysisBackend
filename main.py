import string
from sentiment_analysis.constants import STORAGE_BUCKET
from fastapi import FastAPI, Body
from utils import *

from sentiment_analysis.models import *
from sentiment_analysis.sentiment_analysis import get_sentiment, retrain_model

app = FastAPI()

@app.post("/add_review/")
async def add_review(review: Review = Body(...)):
    retrain_model(review)
    return review

@app.get("/get_review/{review}")
async def get_review(review: str):
    prediction = get_sentiment(review)
    return "Positive Review" if prediction == 1 else "Negative Review"
