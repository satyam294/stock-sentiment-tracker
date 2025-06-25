import pandas as pd
df = pd.read_csv("data/news_by_stock/GOOGL_headlines.csv")
print(df["date"].unique())
