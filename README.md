# Sentiment Analysis

## Introduction

This is a simple sentiment analysis end to end model built using keras library. This code predicts whether the entered review is a postive review or a negative review and then retrains the model to take into account the feedback given. 

## How to run
If you wish to run this model locally, just start the uvicorn server in terminal using `uvicorn main:app` and go to `http://127.0.0.1:8000` in your browser.

## What all does the code do?

output : After obtaining the review entered by user, prediction is shown about whether the review entered was accurate or not.

retrain : After receiveing the feedback from user, the model is retrained to reinforce the correct prediction(in case of both correct or false prediction).

firebase tflite upload which can be then directly used in android applications

## Code structure

main.py consists of request body named 'get_review' which is called using ajax on click of the Predict_Sentiment button. The request body calls 'get_sentiment(review)' function. get_sentiment(review) function is written in sentimental_analysis.py This function loads the saved model using load_model(), loads saved tokenizer using load_tokenizer() and then predicts the review by passing inputs to the model using predict_sentiment(review,tokenizer,model).

The prediction stating whether the review was positive or negative is then displayed in a new feedback form. The feedback form asks the user for feedback whether the originally entered review was actually a positive review or a negative review. On the basis of this feedback entered by the user the model is then retrained.

For retraining the model, feedback is passed via API call to 'add_review'. Add review calls retrain_model(review). retrain_model(review) is present in sentimental_analysis.py This function fits the model on new input and then saves the updated model. 

The updated model is then passed to upload_model(model) present in firebase_upload.py where the model is converted to tflite version before finally publishing the model on firebase. The published tflite model can then directly be used in android applications to make predictions.

## Working
![](https://i.imgur.com/1fLn7cF.png)  
![](https://i.imgur.com/FiRnps9.png)

![](https://i.imgur.com/cnaXAEC.png)


### [Star](https://github.com/Priyansh-Kedia/SentimentAnalysisBackend/stargazers) this repo if you like it. 


### The template was provided by [ColorLib](https://colorlib.com/wp/templates/)
