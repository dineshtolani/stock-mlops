import pandas as pd
import os

def add_features(filepath: str):
    """
    Add technical indicators like Moving Average, Returns.
    """
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)

    # Ensure numeric columns
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    df["MA_10"] = df["Close"].rolling(window=10).mean()
    df["MA_50"] = df["Close"].rolling(window=50).mean()
    df["Returns"] = df["Close"].pct_change()
    df = df.dropna()

    os.makedirs("data/features", exist_ok=True)
    features_path = filepath.replace("processed", "features").replace("_clean.csv", "_features.csv")
    df.to_csv(features_path)
    return df

if __name__ == "__main__":
    filepath = "data/processed/RELIANCE.NS_clean.csv"
    features_df = add_features(filepath)
    print(features_df.head())
