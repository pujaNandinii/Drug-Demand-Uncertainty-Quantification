from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("medicine_model.pkl")

class InputData(BaseModel):
    day: int
    month: int
    day_of_week: int
    is_weekend: int
    lag_1: float
    lag_7: float
    rolling_mean_7: float
    quarter: int
    day_of_year: int
    rolling_std_7: float


@app.post("/predict")
def predict(data: InputData):
    values = pd.DataFrame([{
        "day": data.day,
        "month": data.month,
        "day_of_week": data.day_of_week,
        "is_weekend": data.is_weekend,
        "lag_1": data.lag_1,
        "lag_7": data.lag_7,
        "rolling_mean_7": data.rolling_mean_7,
        "quarter": data.quarter,
        "day_of_year": data.day_of_year,
        "rolling_std_7": data.rolling_std_7
    }])

    prediction = model.predict(values)[0]

    buffer = prediction * 0.15

    lower = round(prediction - buffer, 2)
    upper = round(prediction + buffer, 2)

    recommended_stock = round(upper)

    if recommended_stock > prediction * 1.2:
        risk = "high"
    elif recommended_stock > prediction * 1.1:
        risk = "medium"
    else:
        risk = "low"

    return {
        "prediction": float(round(prediction, 2)),
        "lower": float(lower),
        "upper": float(upper),
        "recommended_stock": int(recommended_stock),
        "risk": risk,
        "insight": "Maintain buffer stock"
    }