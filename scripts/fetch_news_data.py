from time import sleep
import requests
import os
import pandas as pd
from datetime import datetime, timedelta
from config import FINNHUB_API_KEY, DAYS

def get_news_for_stock(ticker, name):
    print(f"\n... Fetching news for {ticker} ...")

    end_date = datetime.now()
    start_date = end_date - timedelta(days=DAYS)

    url = (
        f"https://finnhub.io/api/v1/company-news?symbol={ticker}" 
        f"&from={start_date.strftime('%Y-%m-%d')}"
        f"&to={end_date.strftime('%Y-%m-%d')}"
        f"&token={FINNHUB_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    if not isinstance(data, list) or not data:
        print(f"!!! No news found for {ticker} !!! ")
        return

    headlines = []
    for item in data:
        date = datetime.fromtimestamp(item["datetime"]).strftime("%Y-%m-%d")
        title = item.get("headline", "")
        headlines.append({"date": date, "title": title})

    df = pd.DataFrame(headlines)

    os.makedirs("data/news_by_stock", exist_ok=True)
    output_path = f"data/news_by_stock/{ticker}_headlines.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved news headlines for {ticker} to {output_path} ...")
    sleep(1)