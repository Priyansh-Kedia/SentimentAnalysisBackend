from os import name
import string
from sentiment_analysis.constants import STORAGE_BUCKET
from fastapi import FastAPI, Body, Request
from utils import *

from sentiment_analysis.models import *
from sentiment_analysis.sentiment_analysis import get_sentiment, retrain_model

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/css", StaticFiles(directory="ContactUs/css"), name="static")
app.mount("/js", StaticFiles(directory="ContactUs/js"), name="js")
templates = Jinja2Templates(directory="ContactUs")

@app.get("/", response_class=HTMLResponse)
async def get_prediction_page(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


app.mount("/css", StaticFiles(directory="ContactUs/css"), name="static")
app.mount("/js", StaticFiles(directory="ContactUs/js"), name="js")
templates = Jinja2Templates(directory="ContactUs")

@app.get("/retrain_form/{review}/{prediction}", response_class=HTMLResponse)
async def get_prediction_page(request: Request, review: str, prediction: str):
    return templates.TemplateResponse("retrain.html", {"request":request, "review": review, "prediction": prediction})

@app.post("/add_review/")
async def add_review(review: Review = Body(...)):
    retrain_model(review)
    return "Thank you for feedback, model retrained"

@app.get("/get_review/{review}")
async def get_review(review: str):
    prediction = get_sentiment(review)
    return "Positive Review" if prediction == 1 else "Negative Review"
