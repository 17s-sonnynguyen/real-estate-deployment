from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Create FastAPI app
app = FastAPI(title="Real Estate Pool Prediction API")

# Load saved model
model = joblib.load("pool_predictor.pkl")

# Define input structure
class PropertyInput(BaseModel):
    hot_tub: int
    month_num: int

# Home route
@app.get("/")
def home():
    return {"message": "Real Estate Pool Prediction API is running."}

# Prediction route
@app.post("/predict")
def predict(data: PropertyInput):
    input_data = [[data.hot_tub, data.month_num]]
    prediction = model.predict(input_data)[0]

    return {
        "hot_tub": data.hot_tub,
        "month_num": data.month_num,
        "pool_prediction": int(prediction)
    }