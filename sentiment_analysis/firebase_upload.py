from pickle import NONE
import firebase_admin
from firebase_admin import ml
from firebase_admin import credentials
from .constants import *

import tensorflow as tf

class FirebaseUpload():
    def __init__(self):
        self.app = firebase_admin.initialize_app(
        credentials.Certificate('sentiment_analysis/sentimentalanalysis-6350d-firebase-adminsdk-fufv0-a737778f8b.json'),
        options={
            'storageBucket': 'sentimentalanalysis-6350d.appspot.com',
        })

    def prepare_model(self, tflite_format):
        new_model = None

        models_list = ml.list_models(list_filter="tags: {}".format(MODEL_TAG))
    
        if(len(models_list.models) == 0):      
            model = ml.Model(
                display_name= MODEL_HEADER, 
                tags = [MODEL_TAG],
                model_format=tflite_format)
            new_model = ml.create_model(model)

        else:
            model = ml.get_model(models_list[0].model_id)
            model.model_format = tflite_format
            new_model = ml.update_model(model)

        return new_model

    def upload_model(self, model_retrain):
        source = ml.TFLiteGCSModelSource.from_keras_model(model_retrain, app=self.app)
        tflite_format = ml.TFLiteFormat(model_source=source)
        
        new_model = self.prepare_model(tflite_format)
        ml.publish_model(new_model.model_id)