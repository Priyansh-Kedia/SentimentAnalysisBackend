from os import name
from sentiment_analysis.constants import STORAGE_BUCKET
from fastapi import FastAPI, Body, Request, BackgroundTasks
from utils import *

from sentiment_analysis.models import *
from sentiment_analysis.sentiment_analysis import get_sentiment, retrain_model

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from pathlib import Path
import os

current_file = Path(__file__)
current_file_dir = current_file.parent
project_root = current_file_dir.parent
project_root_absolute = project_root.resolve()
print(project_root_absolute)
static_root_absolute = os.path.join(project_root_absolute,"ContactUs")

app = FastAPI()
app.mount("/css", StaticFiles(directory=os.path.join(static_root_absolute,"css")), name="static")
app.mount("/js", StaticFiles(directory=os.path.join(static_root_absolute, "js")), name="js")
templates = Jinja2Templates(directory=os.path.join(static_root_absolute))


@app.get("/", response_class=HTMLResponse)
async def get_prediction_page(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})

@app.get("/retrain_form/{review}/{prediction}", response_class = HTMLResponse)
async def get_prediction_page(request: Request, review: str, prediction: str):
    return templates.TemplateResponse("retrain.html", {"request":request, "review": review, "prediction": prediction})

@app.post("/add_review/")
async def add_review(background_tasks: BackgroundTasks, review: Review = Body(...)):
    background_tasks.add_task(retrain_model, review)
    return "Thank you for feedback, model retrained"

@app.get("/get_review/{review}")
async def get_review(review: str):
    prediction = get_sentiment(review)
    return "Positive Review" if prediction == 1 else "Negative Review"
