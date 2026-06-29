from typing import Optional
from sqlmodel import SQLModel, Field
from src.api.models import DiabetesPredictionBase


class DiabetesPredictionRequest(DiabetesPredictionBase):
    pass


class DiabetesPredictionResponse(DiabetesPredictionBase):
    prediction: int
    probability: float


class DiabetesPredictionRead(DiabetesPredictionBase):
    id: Optional[int] = Field(default=None, primary_key=True)
    prediction: int
    probability: float
    created_at: Optional[str] = None    