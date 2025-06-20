import yfinance as yf
import pandas as pd
portfolio = ["AAPL", "GOOGL", "TSLA"]
st_date = "2024-01-01"
end_date = "2024-02-01"

for ticker_symbol in portfolio:
    try:
        print(f"Extracting data for {ticker_symbol}...")
        tickerObj = yf.Ticker(ticker_symbol)
        df = tickerObj.history(start = st_date,end = end_date, auto_adjust = True)

        if df.empty:
            print(f"No data for {ticker_symbol} !!!")
            continue

        df = df.reset_index()

        df["%Change"] = df["Close"].pct_change() * 100
        df = df[["Date", "Open","High","Low","Close","Volume","%Change"]]

        print(df.head(2))

        df.to_csv(f"data/stock_data/{ticker_symbol}_stock.csv")
        print(f"{ticker_symbol} file saved !!\n")
    except Exception as e:
        print(f"Error with {ticker_symbol} : {e}")
