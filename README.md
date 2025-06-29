# 📈 Stock Sentiment Tracker

A beginner-friendly data science project that analyzes the correlation between **stock price changes** and **news sentiment** for any portfolio of companies you choose.

---

## 🚀 What This Project Does

This tool helps you understand:

* 📉 **How stock prices react to news sentiment**
* 🧠 Uses **VADER** (a simple rule-based sentiment analyzer) to score headlines
* 📊 Calculates the **Pearson correlation** between daily sentiment and stock price % change
* 🗂️ Outputs a final interpretation like:

  ```
  Company: Apple (AAPL)
  Correlation Score: 0.73
  Interpretation: Strong Positive Correlation
  Meaning: Positive news likely increases price
  Confidence: High
  ```

---

## 🧱 How It Works

### 1. **You define your portfolio** in `config.py`

```python
PORTFOLIO = [
    {"ticker": "AAPL", "name": "Apple"},
    {"ticker": "MSFT", "name": "Microsoft"},
    {"ticker": "GOOGL", "name": "Google"}
]
```

### 2. **Pipeline steps handled automatically** in `main.py`:

| Step                 | What It Does                                                |
| -------------------- | ----------------------------------------------------------- |
| 📈 Fetch Price       | Gets daily closing prices for last 30 days using `yfinance` |
| 📰 Fetch News        | Pulls last 2 weeks of headlines using Finnhub API           |
| 😄 Analyze Sentiment | Computes sentiment using VADER                              |
| 🧮 Correlate         | Calculates Pearson correlation between sentiment and price  |

---

## 🧪 Sample Output

```
------ SENTIMENT-PRICE CORRELATION ANALYSIS ------

***  Processing Apple (AAPL)  ***

--------------------------------------
📊 SENTIMENT-PRICE CORRELATION ANALYSIS
Company: Apple (AAPL)
Correlation Score: 0.7342
Average Sentiment Score: 0.2510
Interpretation: Strong Positive Correlation
Meaning: Positive news likely increases price
Confidence: High
--------------------------------------
```

---

## ⚙️ How to Run It Yourself

### 1. **Clone the repository**

```bash
git clone https://github.com/yourusername/stock-sentiment-analyzer.git
cd stock-sentiment-analyzer
```

### 2. **Install dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Get a Finnhub API Key**

* Sign up at [https://finnhub.io](https://finnhub.io)
* Copy your free API key

### 4. \*\*Setup your \*\***`config.py`**

* Copy the example file:

```bash
cp config_example.py config.py
```

* Then add your API key and define your portfolio:

```python
API_KEY = "your_finnhub_api_key"

PORTFOLIO = [
    {"ticker": "AAPL", "name": "Apple"},
    {"ticker": "MSFT", "name": "Microsoft"},
    {"ticker": "GOOGL", "name": "Google"},
    {"ticker": "NVDA", "name": "NVIDIA"}
]

DAYS = 30  # Number of past days for stock data
```

> ✅ Make sure you \*\*do not commit your \*\***`config.py`** to GitHub.

### 5. **Run the main script**

```bash
python main.py
```

---

## 📁 Project Structure

```
.
├── config.py                 # Your API key + portfolio (not included in repo)
├── config_example.py        # Template file
├── main.py                  # Main runner
├── data/
│   ├── daily_avg_sentiment/ # Output sentiment CSVs
│   ├── news_by_stock/       # Fetched news per stock
│   └── stock_data/          # Fetched price data per stock
├── scripts/
│   ├── fetch_price_data.py
│   ├── fetch_news_data.py
│   ├── analyze_sentiment.py
│   └── correlation.py
└── requirements.txt
```

---

## 🙌 Credits

* News data from **[Finnhub API](https://finnhub.io)**
* Stock prices via **[yfinance](https://pypi.org/project/yfinance/)**
* Sentiment scoring via **[NLTK's VADER](https://github.com/cjhutto/vaderSentiment)**

---

## 📌 Notes

* Only recent news (last 1–2 weeks) is analyzed due to API limits.
* Sentiment scoring is basic and works best for clear headlines.
* Correlation doesn’t imply causation — this is for exploration!

---

## 🛡️ License

This project is open-source and free to use. Everybody is encouraged to tweak and upgrade the pipeline to make it more accurate and reliable.
