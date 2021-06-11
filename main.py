from sentiment_analysis.constants import STORAGE_BUCKET
from fastapi import FastAPI, Body
from utils import *

from sentiment_analysis.models import *
from sentiment_analysis.sentiment_analysis import predict_sentiment, retrain_model

app = FastAPI()

@app.post("/add_review/")
async def add_review(review: Review = Body(...)):
    # add code to save tokenizer
    retrain_model(review)
    return review
