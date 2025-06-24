import requests
import pandas as pd
import time
import os
from datetime import datetime, timedelta

API_KEY = "95f4da7ffe6045e8b2042bee548de9fb"
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
        f"https://newsapi.org/v2/everything?"
        f"q={ticker}&from={from_date}&to={to_date}&"
        f"sortBy=publishedAt&language={language}&apiKey={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    stock_headlines = []

    if "articles" in data:
        for article in data["articles"]:
            date = article["publishedAt"][:10]
            title = article["title"]
            source = article["source"]["name"]

            stock_headlines.append({
                "date": date,
                "title": title,
                "source": source
            })
    else:
        print(f"⚠️ No articles found for {ticker}: {data.get('message', 'Unknown error')}")

    # Save to CSV if there's data
    if stock_headlines:
        df = pd.DataFrame(stock_headlines)
        file_path = os.path.join(output_folder, f"{ticker}_headlines.csv")
        df.to_csv(file_path, index=False)
        print(f"✅ Saved {len(df)} headlines to {file_path}")
    else:
        print(f"❌ No data to save for {ticker}.")

    time.sleep(1)  # Respect API rate limits
