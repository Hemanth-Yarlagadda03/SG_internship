"""
    Training a model and then deploying it with FastAPI
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("C:\\Users\\yhlak\\OneDrive\\Documents\\GitHub\\SG_internship\\04March2025\\insurance.csv")

# Encoding
df = pd.get_dummies(df, drop_first=True)

# Split data
X = df.drop("charges", axis=1)
y = df["charges"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, r"C:\Users\yhlak\OneDrive\Documents\GitHub\SG_internship\04March2025\insurance_model.pkl")
print("Model trained and saved!")

