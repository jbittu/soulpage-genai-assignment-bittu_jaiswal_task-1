from tools.fetchers import fetch_latest_news, fetch_stock_data

class DataCollectorAgent:
    """
    Agent 1: Collects company news + stock data.
    """

    def collect(self, company: str, news_limit=5, stock_days=7):
        news = fetch_latest_news(company, limit=news_limit)
        stocks = fetch_stock_data(company, days=stock_days)

        return {
            "company": company,
            "news": news,
            "stock": stocks
        }
