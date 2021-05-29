from pydantic import BaseModel

class Review(BaseModel):
    review: str
    prediction: int

# model save
# tokenizer save
# vocab save