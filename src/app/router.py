from fastapi import APIRouter
from .models import PredictionRequest, PredictionResponse
from .services.ai_model import predict

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def get_prediction(request: PredictionRequest):
    prediction = predict(request.data)
    return {"prediction": prediction}
