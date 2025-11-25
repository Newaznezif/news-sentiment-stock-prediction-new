# src/stock_analysis.py
import pandas as pd

class StockData:
    """Class to load stock CSV data and compute technical indicators."""

    def __init__(self, file_path, date_col="Date"):
        self.file_path = file_path
        self.date_col = date_col
        self.df = self.load()

    def load(self):
        """Load CSV and parse Date column."""
        df = pd.read_csv(self.file_path, parse_dates=[self.date_col])
        df = df.sort_values(self.date_col).reset_index(drop=True)
        return df

    def add_sma(self, window=20):
        self.df[f"SMA_{window}"] = self.df["Close"].rolling(window).mean()
        return self.df

    def add_ema(self, span=20):
        self.df[f"EMA_{span}"] = self.df["Close"].ewm(span=span, adjust=False).mean()
        return self.df

    def add_rsi(self, window=14):
        delta = self.df["Close"].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(window=window, min_periods=1).mean()
        avg_loss = loss.rolling(window=window, min_periods=1).mean()
        rs = avg_gain / avg_loss
        self.df["RSI"] = 100 - (100 / (1 + rs))
        return self.df

    def add_bollinger_bands(self, window=20, num_std=2):
        sma = self.df["Close"].rolling(window).mean()
        std = self.df["Close"].rolling(window).std()
        self.df["BB_upper"] = sma + num_std * std
        self.df["BB_lower"] = sma - num_std * std
        return self.df

    def add_macd(self, short=12, long=26, signal=9):
        ema_short = self.df["Close"].ewm(span=short, adjust=False).mean()
        ema_long = self.df["Close"].ewm(span=long, adjust=False).mean()
        self.df["MACD"] = ema_short - ema_long
        self.df["Signal"] = self.df["MACD"].ewm(span=signal, adjust=False).mean()
        return self.df
