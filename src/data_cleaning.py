import pandas as pd
import os

def clean_stock_data(filepath: str):
    """
    Clean raw stock data.
    - Flatten multi-index headers
    - Fill missing values
    - Remove duplicates
    """
    # Read CSV with multi-index header
    df = pd.read_csv(filepath, header=[0,1], index_col=0, parse_dates=True)

    # Flatten column names (e.g., ('Close','RELIANCE.NS') -> 'Close')
    df.columns = [col[0] for col in df.columns]

    df = df.drop_duplicates()
    df = df.ffill().bfill()

    os.makedirs("data/processed", exist_ok=True)
    cleaned_path = filepath.replace("raw", "processed").replace(".csv", "_clean.csv")
    df.to_csv(cleaned_path)
    return df

if __name__ == "__main__":
    filepath = "data/raw/RELIANCE.NS.csv"
    cleaned_df = clean_stock_data(filepath)
    print(cleaned_df.head())
