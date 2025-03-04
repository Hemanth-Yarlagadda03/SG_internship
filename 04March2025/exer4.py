from fastapi import FastAPI
import pandas as pd
import joblib

# Load trained model
model = joblib.load("insurance_model.pkl")

# Define FastAPI app
app = FastAPI()

# Define feature names used during training
feature_order = ["age", "bmi", "children", "sex_male", "smoker_yes",
                 "region_northwest", "region_southeast", "region_southwest"]

# Define the API route
@app.post("/predict/")
def predict_insurance(age: int, sex: str, bmi: float, children: int, smoker: str, region: str):
    # Convert categorical inputs to one-hot encoding
    data = {
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "sex_male": [1 if sex.lower() == "male" else 0],
        "smoker_yes": [1 if smoker.lower() == "yes" else 0],
        "region_northwest": [1 if region.lower() == "northwest" else 0],
        "region_southeast": [1 if region.lower() == "southeast" else 0],
        "region_southwest": [1 if region.lower() == "southwest" else 0]
    }

    # Convert dictionary to DataFrame
    input_data = pd.DataFrame(data)

    # Ensure the column order matches the trained model
    input_data = input_data[feature_order]

    # Make prediction
    prediction = model.predict(input_data)

    return {"predicted_charges": float(prediction[0])}
