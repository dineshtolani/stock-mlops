import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_model(filepath: str):
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    X = df[["MA_10", "MA_50", "Returns"]]
    y = df["Close"].shift(-1).dropna()
    X = X.iloc[:-1]

    model = LinearRegression()
    model.fit(X, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/saved_model.pkl")
    print("✅ Model trained and saved at models/saved_model.pkl")

if __name__ == "__main__":
    filepath = "data/features/RELIANCE.NS_features.csv"
    train_model(filepath)
