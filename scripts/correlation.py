
import os
import pandas as pd
from scipy.stats import pearsonr
#pandas inbuilt correaltion function can also be used

def interpret_score(score, avg_sentiment):
    if score > 0.7:
        return "Very Strong Positive Correlation", "Very high likelihood that positive news drives price up", "High"
    elif score > 0.5:
        return "Strong Positive Correlation", "Positive news likely increases price", "High"
    elif score > 0.3:
        return "Moderate Positive Correlation", "Some positive relationship between price and sentiment detected", "Medium"
    elif score > 0.2:
        return "Positive Correlation", "Very ittle influence of sentiment on price, not affirmative", "Low"
    elif score > 0.1:
        return "Weak Positive Correlation", "No strong relationship between sentiment and price can be suggested", "Low"
    elif score > 0:
        return "Very Weak Positive Correlation", "Insignificant for any conclusions","None"
    elif score == 0:
        return "No Correlation", "Sentiment and price are unrelated", "None"
    elif score < 0 and avg_sentiment > 0.2:
        return "Unexpected Negative Correlation (price drops with positive sentiment) !!!", "Avg Positive Sentiment but Stock might be suffering fundamentally, leading to price drop", "None"
    elif score < 0 and avg_sentiment < 0:
        return "Unexpected Negative Correlation (price rises with negative sentiment) !!!", "Avg Negative Sentiment. Generally, more negative sentiment in the news, not affecting price too much", "None"
    else : 
        return "Unexpected Negative Correlation", "Negative relationship between sentiment and price", "None"
def compute_correlation(ticker, avg_sentiment):
    print(f"\n ... Correlating sentiment and stock price for {ticker} ...")

    sentiment_path = f"data/daily_avg_sentiment/{ticker}_avg_sentiment.csv"
    price_path = f"data/stock_data/{ticker}_stock.csv"

    if not os.path.exists(sentiment_path) or not os.path.exists(price_path):
        print(f"!!! Missing data files for {ticker}. Skipping...")
        return None, None, None, None

    sentiment_df = pd.read_csv(sentiment_path)
    price_df = pd.read_csv(price_path)

    # ensuring date time columns in both data frames
    sentiment_df["date"] = pd.to_datetime(sentiment_df["date"])
    price_df["date"] = pd.to_datetime(price_df["Date"])

    merged_df = pd.merge(price_df, sentiment_df, on="date", how="inner")

    if merged_df.empty:
        print(f" !!! No overlapping dates for {ticker} to correlate.")
        return None, None, None, None


    corr, _ = pearsonr(merged_df["% Change"], merged_df["compound"])
    label, meaning, confidence = interpret_score(corr, avg_sentiment)

    return corr, label, meaning, confidence
