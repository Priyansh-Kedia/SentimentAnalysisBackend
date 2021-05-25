# FastApi will be used to make the apis, 
# refer to https://fastapi.tiangolo.com/ to read about the same
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def test_endpoint(review: str, is_positive: int,check_prediction: bool ):
    print("Review :",review,"\n")
    print("Review :",is_positive,"\n")
    print("Review :",check_prediction,"\n")
    return 1
