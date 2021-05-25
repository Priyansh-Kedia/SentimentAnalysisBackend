from fastapi import FastAPI, Body
from pydantic import BaseModel

class Review(BaseModel):
    review: str
    is_positive: bool
    correct_prediction: bool

app = FastAPI()

@app.post("/add_review/")
def add_review(review: Review = Body(...)):
    print("Review is ", review.review)
    return review
