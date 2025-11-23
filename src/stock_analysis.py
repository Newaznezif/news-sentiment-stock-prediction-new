import pandas as pd

class StockData:
    """Load and compute technical indicators for stock data."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(file_path, parse_dates=["Date"])
        self.df = self.df.sort_values("Date").reset_index(drop=True)

    def add_sma(self, window=5):
        """Add Simple Moving Average."""
        self.df[f"SMA_{window}"] = self.df["Close"].rolling(window).mean()
        return self.df

    def add_rsi(self, window=14):
        """Compute RSI (example implementation without TA-Lib)."""
        delta = self.df["Close"].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(window=window, min_periods=1).mean()
        avg_loss = loss.rolling(window=window, min_periods=1).mean()
        rs = avg_gain / avg_loss
        self.df["RSI"] = 100 - (100 / (1 + rs))
        return self.df
