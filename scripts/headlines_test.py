import requests
import pandas as pd
import time
import os
from datetime import datetime, timedelta

API_KEY = "d1dqoc9r01qpp0b3gv60d1dqoc9r01qpp0b3gv6g"
end_date = datetime.today()
start_date = end_date - timedelta(days=30)
from_date = start_date.strftime("%Y-%m-%d")
to_date = end_date.strftime("%Y-%m-%d")
language = "en"
portfolio = ["AAPL", "MSFT", "GOOGL"]

# Folder to store output
output_folder = "data/news_by_stock"
os.makedirs(output_folder, exist_ok=True)

for ticker in portfolio:
    print(f"\nFetching news for {ticker}...")

    url = (
    f"https://finnhub.io/api/v1/company-news?"
    f"symbol={ticker}&from={from_date}&to={to_date}&token={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    #print(f"\n📦 Raw response for {ticker}:")
    #print(data)

    #if not isinstance(data, list):
    #   print(f"❌ Error for {ticker}: {data}")
    #   continue


    headlines = []

    for item in data:
        timestamp = datetime.fromtimestamp(item["datetime"]).strftime("%Y-%m-%d")
        headline = item["headline"]
        source = item.get("source", "")

        headlines.append({
            "date": timestamp,
            "title": headline,
            "source": source,
        })

    if headlines:
        df = pd.DataFrame(headlines)
        file_path = os.path.join(output_folder, f"{ticker}_headlines.csv")
        df.to_csv(file_path, index=False)
        print(f"✅ Saved {len(df)} headlines to {file_path}")
    else:
        print(f"❌ No news found for {ticker}.")

    time.sleep(1)
    