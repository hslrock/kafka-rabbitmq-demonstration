# You can define your Pydantic models here
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    data: list


class PredictionResponse(BaseModel):
    prediction: str
