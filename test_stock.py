from dotenv import load_dotenv
load_dotenv()

from tools.fetchers import fetch_stock_data

print(fetch_stock_data("GOOGL"))
