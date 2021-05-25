from fastapi import FastAPI, Body

from sentiment_analysis.models import *

app = FastAPI()

@app.post("/add_review/")
def add_review(review: Review = Body(...)):
    print("Review is ", review.review)
    return review
