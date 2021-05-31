from nltk.corpus import stopwords

import string
from os import listdir
from collections import Counter

from keras.preprocessing.text import Tokenizer
from keras import models
from numpy import array

from sentiment_analysis.constants import *

from keras.models import *

import pickle

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
    
    # filter out the stop words
    stop_words = set(stopwords.words("english"))
    tokens = [w for w in tokens if not w in stop_words]

    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 1]
    return tokens

def extract_XTrain(review,vocab,tokenizer):
    tokens = clean_doc(review.review)
    tokens = [w for w in tokens if w in vocab]
    line = ' '.join(tokens)
    return tokenizer.texts_to_matrix([line],mode = 'freq')

def extract_ytrain(review):
    return array([review.prediction])

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

def retrain_model(review):
    # create the tokenizer
    # tokenizer = Tokenizer()
    # fit the tokenizer on the values
    # docs = clean_doc(review.review)

    # tokenizer.fit_on_texts(docs)

    # XTrain = tokenizer.texts_to_matrix(docs, mode='freq')
    # ytrain = [review.prediction]

    # print(XTrain, ytrain)

    model = load_model(MODEL_NAME)

    tokenizer = load_tokenizer(TOKENIZER_NAME)

    vocab = load_vocab(VOCAB_NAME)
    
    # predict_sentiment(review.review, tokenizer, model)
    XTrain = extract_XTrain(review,vocab,tokenizer)
    ytrain = extract_ytrain(review)
    model.fit(XTrain, ytrain, epochs=50, verbose=2)

    # model.save(MODEL_NAME)
    
