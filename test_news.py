from dotenv import load_dotenv
load_dotenv()  
from tools.fetchers import fetch_latest_news

print(fetch_latest_news("Google"))
