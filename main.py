import os
from scripts.fetch_price_data import get_stock_data
from scripts.fetch_news_data import get_news_for_stock
from scripts.analyze_sentiment import compute_daily_sentiment
from scripts.correlation import compute_correlation
from config import PORTFOLIO


print("\n ------ SENTIMENT-PRICE CORRELATION ANALYSIS ------ \n")

for stock in PORTFOLIO:
    ticker = stock["ticker"]
    name = stock["name"]

    print(f"*** Processing {name} ({ticker}) ***")

    try:
        # 1. Fetch price data
        get_stock_data(ticker)

        # 2. Fetch news headlines
        get_news_for_stock(ticker, name)

        # 3. Analyze sentiment
        raw_avg_sentiment = compute_daily_sentiment(ticker)

        avg_sentiment = float(raw_avg_sentiment)

        # 4. Correlate
        correlation_score, interpretation, meaning, confidence = compute_correlation(ticker, avg_sentiment)

        print("\n--------------------------------------")
        print("📊 SENTIMENT-PRICE CORRELATION ANALYSIS")
        print(f"-> Company: {name} ({ticker})")
        print(f"-> Correlation Score: {correlation_score:.4f}")
        print(f"-> Average Sentiment Score: {avg_sentiment:.4f}")
        print(f"-> Interpretation: {interpretation}")
        print(f"-> Meaning: {meaning}")
        print(f"-> Confidence: {confidence}")
        print("--------------------------------------\n")

    except Exception as e:
        print(f"!!! Error processing {name}: {e}\n")
