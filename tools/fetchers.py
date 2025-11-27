import os
import requests
from datetime import datetime, timedelta


def fetch_latest_news(company: str, limit=5):
    api_key = os.getenv("NEWSAPI_KEY")
    if not api_key:
        raise ValueError("Missing NEWSAPI_KEY in .env")

    url = "https://newsapi.org/v2/everything"
    params = {
        "qInTitle": company,       
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": limit,
        "apiKey": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "articles" not in data:
        return [{
            "title": "No articles found",
            "summary": "",
            "published_at": "",
            "url": ""
        }]

    news = []
    for article in data["articles"]:
        news.append({
            "title": article.get("title", ""),
            "summary": article.get("description", ""),
            "published_at": article.get("publishedAt", ""),
            "url": article.get("url", "")
        })

    return news[:limit]





def fetch_stock_data(company: str, days=7):
    api_key = os.getenv("ALPHA_VANTAGE_KEY")
    if not api_key:
        raise ValueError("Missing ALPHA_VANTAGE_KEY in .env")

    url = (
        "https://www.alphavantage.co/query?"
        f"function=TIME_SERIES_DAILY&symbol={company}&apikey={api_key}"
    )

    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" not in data:
        return {
            "symbol": company,
            "prices": [],
            "latest_close": None,
            "7d_change_pct": None
        }

    ts = data["Time Series (Daily)"]
    sorted_dates = sorted(ts.keys(), reverse=True)

    prices = []
    for date in sorted_dates[:days]:
        close_price = float(ts[date]["4. close"])
        prices.append({"date": date, "close": close_price})

    # Compute change %
    if len(prices) >= 2:
        first = prices[-1]["close"]
        last = prices[0]["close"]
        change_pct = round(((last - first) / first) * 100, 2)
    else:
        change_pct = 0

    return {
        "symbol": company,
        "prices": prices,
        "latest_close": prices[0]["close"] if prices else None,
        "7d_change_pct": change_pct
    }
