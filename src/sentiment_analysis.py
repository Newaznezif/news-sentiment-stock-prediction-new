# src/sentiment_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure VADER lexicon is available
nltk.download('vader_lexicon', quiet=True)

class SentimentAnalysis:
    """Analyze news sentiment and correlate with stock data."""

    def __init__(self, news_df: pd.DataFrame, stock_df: pd.DataFrame):
        self.news_df = news_df.copy()
        self.stock_df = stock_df.copy()
        self.sid = SentimentIntensityAnalyzer()

    def compute_sentiment(self) -> pd.DataFrame:
        """Compute daily average sentiment from news headlines."""
        self.news_df['date'] = pd.to_datetime(self.news_df['date'])
        self.news_df['sentiment'] = self.news_df['headline'].apply(
            lambda x: self.sid.polarity_scores(str(x))['compound']
        )
        daily_sentiment = self.news_df.groupby('date')['sentiment'].mean().reset_index()
        daily_sentiment.rename(columns={'sentiment':'avg_sentiment'}, inplace=True)
        return daily_sentiment

    def merge_with_stock(self, daily_sentiment: pd.DataFrame) -> pd.DataFrame:
        self.stock_df['Date'] = pd.to_datetime(self.stock_df['Date'])
        self.stock_df['daily_return'] = self.stock_df['Close'].pct_change()
        merged = pd.merge(
            self.stock_df, daily_sentiment,
            left_on='Date', right_on='date', how='left'
        )
        merged['avg_sentiment'] = merged['avg_sentiment'].fillna(method='ffill')
        merged.dropna(inplace=True)
        return merged

    def correlation(self, merged: pd.DataFrame) -> float:
        return merged['daily_return'].corr(merged['avg_sentiment'])

    def plot_sentiment_vs_stock(self, merged: pd.DataFrame):
        fig, ax1 = plt.subplots(figsize=(12,6))
        ax1.plot(merged['Date'], merged['daily_return'], color='blue', label='Daily Return')
        ax1.set_ylabel("Daily Return", color='blue')
        ax2 = ax1.twinx()
        ax2.plot(merged['Date'], merged['avg_sentiment'], color='red', label='Avg Sentiment')
        ax2.set_ylabel("Avg Sentiment", color='red')
        fig.tight_layout()
        plt.show()
