from dotenv import load_dotenv
import os

load_dotenv()

print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))
print("NEWSAPI_KEY:", os.getenv("NEWSAPI_KEY"))
print("ALPHA_VANTAGE_KEY:", os.getenv("ALPHA_VANTAGE_KEY"))
