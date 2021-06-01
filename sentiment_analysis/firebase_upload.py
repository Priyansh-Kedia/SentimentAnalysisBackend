
class FirebaseUpload():
    def __init__(self):
        print("called here")
        import firebase_admin
        from firebase_admin import ml
        from firebase_admin import credentials

        firebase_admin.initialize_app(
        credentials.Certificate('/path/to/your/service_account_key.json'),
        options={
            'storageBucket': 'your-storage-bucket',
        })

    def upload_model(self, model):
        # upload the model
        # first check if the model already exists in firebase
        # if it exists, update it, otherwise create new