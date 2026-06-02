import yfinance as yf
import os

def download_stock_data(symbol: str, start: str = "2020-01-01", end: str = None):
    """
    Download historical stock data from Yahoo Finance.
    Args:
        symbol (str): Stock ticker (e.g., 'RELIANCE.NS')
        start (str): Start date (YYYY-MM-DD)
        end (str): End date (YYYY-MM-DD), defaults to today
    Returns:
        DataFrame: OHLCV data
    """
    df = yf.download(symbol, start=start, end=end)
    if df.empty:
        raise ValueError(f"No data found for {symbol}")
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv(f"data/raw/{symbol}.csv")
    return df

if __name__ == "__main__":
    stock = "RELIANCE.NS"
    data = download_stock_data(stock)
    print(data.head())
