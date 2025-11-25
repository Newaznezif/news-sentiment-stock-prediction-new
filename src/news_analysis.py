# src/news_analysis.py
import pandas as pd
import re

class NewsData:
    """Class to load and preprocess news data."""

    def __init__(self, file_path, date_col="date", text_col="headline"):
        """
        file_path: path to news CSV
        date_col: column name for date
        text_col: column name for news text
        """
        self.file_path = file_path
        self.date_col = date_col
        self.text_col = text_col
        self.df = self.load()
        self.clean_text()

    def load(self):
        """Load CSV and parse date column."""
        df = pd.read_csv(self.file_path, parse_dates=[self.date_col])
        df = df.sort_values(self.date_col).reset_index(drop=True)
        return df

    def clean_text(self, column=None):
        """Clean text data: remove extra spaces, lowercase, etc."""
        column = column or self.text_col
        self.df[column] = (
            self.df[column]
            .astype(str)
            .str.lower()
            .apply(lambda x: re.sub(r'\s+', ' ', x))
        )
        return self.df
