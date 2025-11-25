News Sentiment & Stock Movement Analysis
A multi-stage analytics project exploring how financial news sentiment correlates with stock price movement.
Author: Newaz Nezif
Date: November 2025
Repository: https://github.com/YourGitHubUsername/news-sentiment-stock-prediction-new
________________________________________
📌 Project Overview
This project investigates whether financial news sentiment influences stock market movements.
It brings together:
•	News analysis
•	Sentiment scoring
•	Stock technical analysis
•	Correlation modeling
•	Rolling time-series relationships
The goal is to build an analytical foundation suitable for:
•	Trading insights
•	Quantitative research
•	Predictive modeling
•	Sentiment-driven investment signals
________________________________________
📁 Repository Structure
news-sentiment-stock-prediction-new/
├── Datas/
│   ├── newsData/                     # Raw news CSV data
│   ├── processed/                    # Cleaned outputs (sentiment, merged datasets, correlation)
│   └── yfinance_data/Data/           # Stock price CSV files
│
├── notebooks/                        # All Jupyter Notebooks
│   ├── task1_news_analysis.ipynb
│   ├── EDA_Descriptive_Stats.ipynb
│   ├── EDA_Text_Analysis.ipynb
│   ├── EDA_TimeSeries_Publisher.ipynb
│   ├── EDA_Task2_Quantitative.ipynb
│   ├── EDA_Task3_Sentiment.ipynb
│   └── test.py
│
├── src/                              # Reusable Python package
│   ├── news_analysis.py              # Cleaning, text processing, publisher analysis
│   ├── sentiment_analysis.py         # Sentiment scoring & aggregation
│   ├── stock_analysis.py             # Technical indicators, stock trend analysis
│   ├── utils.py                      # Correlation, merging, helper utilities
│   └── __init__.py
│
├── scripts/                          # Optional automation scripts
├── tests/                            # Unit tests
│
├── README.md
├── requirements.txt
└── .gitignore
________________________________________
🚀 Setup Instructions
1. Clone the Repository
git clone https://github.com/YourGitHubUsername/news-sentiment-stock-prediction-new.git
cd news-sentiment-stock-prediction-new
2. Create a Virtual Environment
python -m venv venv
Activate:
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
________________________________________
📊 Task 1 — News Data Analysis
Objectives
•	Load raw analyst rating data.
•	Convert timestamps & clean text.
•	Perform exploratory analysis.
•	Identify top publishers & publication trends.
Key Outputs
✔ Top publishers
✔ Headline length distribution
✔ Daily publication counts
✔ Text statistics
Relevant Files
•	notebooks/task1_news_analysis.ipynb
•	notebooks/EDA_Descriptive_Stats.ipynb
•	Datas/processed/top_publishers.csv
•	Datas/processed/headline_length_summary.csv
________________________________________
📈 Task 2 — Stock Price Analysis
Objectives
•	Load stock price data (AAPL, MSFT, AMZN, GOOG, META, NVDA).
•	Compute technical indicators:
o	Moving Averages (MA10, MA20, MA50)
o	RSI
o	MACD
•	Visualize trend patterns.
Key Methods Used
•	Rolling windows
•	Technical indicator overlays
•	Comparative analysis across multiple stocks
Relevant Files
•	notebooks/EDA_Task2_Quantitative.ipynb
•	src/stock_analysis.py
•	Raw data under: Datas/yfinance_data/Data/
________________________________________
🧠 Task 3 — Sentiment vs Stock Movement (Core of the Project)
Objectives
•	Compute sentiment scores for news.
•	Merge news sentiment with stock returns.
•	Compute rolling correlations.
•	Explore lagged effects (sentiment leading price or vice-versa).
•	Visualize relationships.
________________________________________
Key Steps in Task 3
1. Sentiment Scoring
Using VADER:
•	Compound sentiment
•	Positive/negative/neutral
•	Daily average sentiment
•	Smoothed time-series
2. Merging With Stock Data
Merged on:
Date → (sentiment + daily returns)
Output file:
Datas/processed/merged_sentiment_stock.csv
3. Rolling Correlation
Default windows:
•	10-day
•	30-day
•	60-day (optional)
Output file:
Datas/processed/rolling_correlation.csv
4. Visualizations
•	Sentiment vs returns scatter
•	Rolling correlation time-series line chart
•	Heatmap of sentiment vs return lags
•	Sentiment vs price trend overlay
Relevant Files
•	notebooks/EDA_Task3_Sentiment.ipynb
•	src/sentiment_analysis.py
•	src/utils.py
________________________________________
🧪 Usage Example (From Code)
from src.news_analysis import NewsData
from src.stock_analysis import StockData
from src.sentiment_analysis import SentimentAnalyzer
from src.utils import merge_news_stock, compute_rolling_corr

# Load news
news = NewsData("Datas/newsData/raw_analyst_ratings.csv")
news.clean()

# Sentiment
sent = SentimentAnalyzer(news.df)
sent.compute_vader_scores()
daily_sent = sent.aggregate_daily_sentiment()

# Load stock
aapl = StockData("Datas/yfinance_data/Data/AAPL.csv")
aapl.add_technical_indicators()

# Merge
merged = merge_news_stock(daily_sent, aapl.df)

# Rolling correlation
corr = compute_rolling_corr(merged, window=30)
________________________________________
🌿 Branching Strategy
Branch	Purpose
main	Stable, final outputs for demo/report
task-1	All news cleaning + publisher analysis
task-2	Technical indicator development
task-3	Sentiment scoring + correlation modeling
refactor-src	Organizing modules into src/
Workflow:
1.	Work in task branch
2.	Commit changes
3.	Push to GitHub
4.	Create Pull Request
5.	Merge into main once stable
________________________________________
💡 Future Improvements
•	Add LSTM/Transformer sentiment models
•	Build predictive machine-learning models
•	Add dashboards with Dash/Streamlit
•	Expand dataset (CNBC, Reuters, Yahoo Finance news)
•	Improve lag modeling
•	Deploy an API endpoint for sentiment signals
________________________________________
📬 Contact
For collaboration or feedback:
Newaz Nezif  — Analyst
________________________________________
✔ Final Note
This repository now supports end-to-end sentiment + stock correlation analysis, with reusable modules, clear notebooks, and a clean branching strategy.

