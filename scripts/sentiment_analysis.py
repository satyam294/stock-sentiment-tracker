import nltk
import pandas as pd
import os

from datetime import datetime, timedelta
from nltk.sentiment.vader import SentimentIntensityAnalyzer
portfolio = ["AAPL", "MSFT", "GOOGL"]

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()
output_folder = "data/daily_avg_sentiment"
def compound_score(text):
    scores = sia.polarity_scores(str(text))
    return scores["compound"]

for stock in portfolio: 
    print(f"Calculating scores for {stock} ...")
    csv_path = f"data/news_by_stock/{stock}_headlines.csv"

    df = pd.read_csv(csv_path)

    # Convert 'date' column to datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Drop rows with invalid or missing dates
    df = df.dropna(subset=["date"])

    # Filter to last 30 days only
    cutoff = datetime.today() - timedelta(days=30)
    df = df[df["date"] >= cutoff]

    df["compound"] = df["title"].apply(compound_score)

    strong_sentiment = df[(df["compound"]>= 0.3) | (df["compound"] <= -0.1)]

    daily_sentiment = strong_sentiment.groupby("date")["compound"].mean().reset_index()

    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, f"{stock}_avg_sentiment.csv")

    daily_sentiment.to_csv(file_path, index = False)

    print(f"Saved {len(daily_sentiment)} rows of {stock}")

