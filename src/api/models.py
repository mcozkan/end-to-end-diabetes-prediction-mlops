from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class DiabetesPredictionBase(SQLModel):
    pregnancies: int
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    diabetes_pedigree_function: float
    age: int


#Create table DiabetesPrediction in the database with the following fields based on the base model DiabetesPredictionBase. 
# The table will have an additional field id as the primary key, prediction, probability, and created_at with a default value of the current UTC time.
class DiabetesPrediction(DiabetesPredictionBase, table = True):
    __tablename__ = "diabetes_predictions"
    id: Optional[int] = Field(default = None, primary_key = True)
    prediction: int
    probability: float
    created_at : datetime = Field(default_factory = datetime.utcnow)
