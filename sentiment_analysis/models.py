from pydantic import BaseModel

class Review(BaseModel):
    review: str
    prediction: int