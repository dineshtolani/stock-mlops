import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_with_mlflow(filepath: str):
    # Load features
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    X = df[["MA_10", "MA_50", "Returns"]]
    y = df["Close"].shift(-1).dropna()
    X = X.iloc[:-1]

    # Start MLflow run
    mlflow.set_experiment("Stock_Prediction")
    with mlflow.start_run():
        model = LinearRegression()
        model.fit(X, y)

        # Log parameters
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_param("features", ["MA_10", "MA_50", "Returns"])

        # Log metrics
        score = model.score(X, y)
        mlflow.log_metric("r2_score", score)

        # Save model
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, "models/saved_model.pkl")

        # Log model artifact
        mlflow.sklearn.log_model(model, "linear_model")

        print(f"Model trained with R² score: {score}")

if __name__ == "__main__":
    filepath = "data/features/RELIANCE.NS_features.csv"
    train_with_mlflow(filepath)
