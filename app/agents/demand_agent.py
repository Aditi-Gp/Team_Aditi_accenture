# demand_agent.py — Predicts product demand using ML model

import pandas as pd
import sqlite3
import pickle
from sklearn.ensemble import RandomForestRegressor
import os

DB_PATH = "data/retail_inventory.db"
MODEL_PATH = "models/demand_rf_model.pkl"

def fetch_demand_data():
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT * FROM demand_forecasting"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def preprocess(df):
    df = df.copy()
    categorical_cols = ['Promotions', 'Seasonality Factors', 'External Factors', 'Demand Trend', 'Customer Segments']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df['Day'] = df['Date'].dt.day
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df.drop(columns=['Date'], inplace=True)
    return df

def train_model():
    df = fetch_demand_data()
    df = preprocess(df)
    X = df.drop(columns=['Sales Quantity'])
    y = df['Sales Quantity']
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)
    print("Demand prediction model trained and saved.")

def predict_demand(input_data: dict):
    if not os.path.exists(MODEL_PATH):
        train_model()
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    input_df = pd.DataFrame([input_data])
    input_df = preprocess(input_df)
    prediction = model.predict(input_df)[0]
    return prediction

if __name__ == "__main__":
    train_model()
