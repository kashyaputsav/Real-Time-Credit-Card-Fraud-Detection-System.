from fastapi import FastAPI
import joblib
import numpy as np
import shap

app = FastAPI()

model = joblib.load("../artifacts/model.pkl")
threshold = joblib.load("../artifacts/threshold.pkl")

explainer = shap.TreeExplainer(model)

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.post("/predict")
def predict(data: dict):
    values = list(data.values())
    features = np.array(values).reshape(1, -1)

    prob = model.predict_proba(features)[0][1]
    pred = int(prob >= threshold)

    shap_values = explainer.shap_values(features)

    return {
        "fraud_probability": float(prob),
        "prediction": pred,
        "shap_values": shap_values[0].tolist()
    }