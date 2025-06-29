import yfinance as yf
import os
import pandas as pd
from datetime import datetime, timedelta
from config import DAYS

def get_stock_data(ticker):
    print(f"\n... Fetching price data for {ticker} ...")

    end_date = datetime.today()
    start_date = end_date - timedelta(days=DAYS)

    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"), auto_adjust=True)

    if df.empty:
        print(f"!!! No data for {ticker} !!!")
        return

    df["% Change"] = df["Close"].pct_change() * 100
    df = df.dropna()
    df.reset_index(inplace=True)
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

    os.makedirs("data/stock_data", exist_ok=True)
    output_path = f"data/stock_data/{ticker}_stock.csv"
    df[["Date", "% Change"]].to_csv(output_path, index=False)
    print(f"Saved stock data for {ticker} to {output_path} ...")
