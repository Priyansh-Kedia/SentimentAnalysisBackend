from fastapi import FastAPI, Body

from sentiment_analysis.models import *
from sentiment_analysis.sentiment_analysis import retrain_model

app = FastAPI()

@app.post("/add_review/")
async def add_review(review: Review = Body(...)):
    # add code to save tokenizer
    retrain_model(review)
    return review
