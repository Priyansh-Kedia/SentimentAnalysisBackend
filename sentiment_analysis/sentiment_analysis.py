from firebase_admin.ml import update_model

import string
from os import listdir
from collections import Counter

from keras.preprocessing.text import Tokenizer
from keras import models
from numpy import array
from pydantic.main import prepare_config

from sentiment_analysis.constants import *

from keras.models import *

import pickle

from .firebase_upload import *


# load model
def load_model(model_name):
    return models.load_model(model_name)

# load model
def load_tokenizer(tokenizer_name):
    with open(tokenizer_name, 'rb') as handle:
        tokenizer = pickle.load(handle)
    return tokenizer

# load model
def load_vocab(vocab_name):
    file_object = open(vocab_name, 'r')
    return file_object.read()

# Convert doc to token
def clean_doc(doc):
    # Splits the words by space
    tokens = doc.split()
    # remove punctuation from each token
    table = str.maketrans('','', string.punctuation)
    tokens = [w.translate(table) for w in tokens]

    # remove the tokens which are not alphabetic
    tokens = [word for word in tokens if word.isalpha()]
    
    #To read stopwords saved in txt file instead of using nltk.corpus
    with open('StopWords.txt','rb') as f:
        stop_words = pickle.load(f)

    tokens = [w for w in tokens if not w in stop_words]

    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 1]
    return tokens

def valid_tokens(tokens,vocab):
    # filter by vocab
    tokens = [w for w in tokens if w in vocab]
    # convert list to string
    line = ' '.join(tokens)
    return line

def prepare_data(review,vocab,tokenizer):
    # clean
    tokens = clean_doc(review.review)
    # filter by vocab
    line = valid_tokens(tokens,vocab)
    # convert to matrix
    XTrain = tokenizer.texts_to_matrix([line],mode='freq')
    #convert to array
    ytrain = array([review.prediction])

    return XTrain,ytrain

def predict_sentiment(review, tokenizer, model):
    # clean
    tokens = clean_doc(review)
    # filter by vocab
    tokens = [w for w in tokens if w]
    # convert to line
    line = ' '.join(tokens)
    # encode
    encoded = tokenizer.texts_to_matrix([line], mode='freq')

    # prediction
    yhat = model.predict(encoded, verbose=0)
    return round(yhat[0,0])

def get_sentiment(review):
    model = load_model(MODEL_NAME)
    tokenizer = load_tokenizer(TOKENIZER_NAME)
    sentiment = predict_sentiment(review,tokenizer,model)
    return sentiment

def retrain_model(review):

    model = load_model(MODEL_NAME)

    tokenizer = load_tokenizer(TOKENIZER_NAME)

    vocab = load_vocab(VOCAB_NAME)
    
    # extract XTrain and ytrain
    XTrain,ytrain = prepare_data(review,vocab,tokenizer)
    
    model.fit(XTrain, ytrain, epochs=50, verbose=2)
    
    # update saved model
    model.save(MODEL_NAME)
    
    firebase_upload = FirebaseUpload()
    firebase_upload.upload_model(model)
