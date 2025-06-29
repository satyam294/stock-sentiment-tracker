
import nltk
import os
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def get_compound_score(text):
    scores = sia.polarity_scores(str(text))
    return scores["compound"]

def compute_daily_sentiment(ticker):
    print(f"\n... Analyzing sentiment for {ticker} ...")

    input_path = f"data/news_by_stock/{ticker}_headlines.csv"
    df = pd.read_csv(input_path)

    # Compute compound sentiment score for each headline
    df["compound"] = df["title"].apply(get_compound_score)

    # Filter to strong sentiment headlines only
    strong_sentiment = df[(df["compound"] >= 0.3) | (df["compound"] <= -0.3)]

    # Group by date and compute average sentiment
    daily_sentiment = strong_sentiment.groupby("date")["compound"].mean().reset_index()
  
    #calculate overall avg sentiment
    raw_avg_sentiment = daily_sentiment["compound"].mean()
    avg_sentiment = float(raw_avg_sentiment)
    
    # Save the result
    os.makedirs("data/daily_avg_sentiment", exist_ok=True)
    output_path = f"data/daily_avg_sentiment/{ticker}_avg_sentiment.csv"
    daily_sentiment.to_csv(output_path, index=False)
    print(f"Saved average daily sentiment for {ticker} to {output_path} ...")

    if len(daily_sentiment) == 0:
        return 0.0

    return avg_sentiment


