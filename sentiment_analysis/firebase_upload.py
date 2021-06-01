from pickle import NONE
import firebase_admin
from firebase_admin import ml
from firebase_admin import credentials
from .constants import *
class FirebaseUpload():
    def __init__(self):
        firebase_admin.initialize_app(
        credentials.Certificate('sentiment_analysis\sentimentalanalysis-6350d-firebase-adminsdk-fufv0-588e50de0f.json'),
        options={
            'storageBucket': 'gs://sentimentalanalysis-6350d.appspot.com',
        })

    def model_prepare(tflite_format):
        new_model = None

        models_list = ml.list_models(list_filter=[MODEL_TAG])
        
        if(len(models_list)==0):      
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
        # Convert the model to TensorFlow Lite and upload it to Cloud Storage
        source = ml.TFLiteGCSModelSource.from_keras_model(model_retrain)
        tflite_format = ml.TFLiteFormat(model_source=source)

        new_model = self.model_prepare(tflite_format)
        
        ml.publish_model(new_model.model_id)