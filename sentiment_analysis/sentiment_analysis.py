from nltk.corpus import stopwords

import string
from os import listdir
from collections import Counter

from keras.preprocessing.text import Tokenizer
from keras import models
from numpy import array


from .constants import MODEL_NAME

from .models import *

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
    tokenizer = Tokenizer()
    # fit the tokenizer on the values
    # docs = clean_doc(review.review)

    # tokenizer.fit_on_texts(docs)

    # XTrain = tokenizer.texts_to_matrix(docs, mode='freq')
    # ytrain = [review.prediction]

    # print(XTrain, ytrain)
    model = models.load_model(MODEL_NAME)

    predict_sentiment(review.review, tokenizer, model)
    # model.fit(XTrain, ytrain, epochs=50, verbose=2)

    # model.save(MODEL_NAME)
    