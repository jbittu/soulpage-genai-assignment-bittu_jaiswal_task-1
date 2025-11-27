from dotenv import load_dotenv
load_dotenv()

from orchestrator import Orchestrator

orch = Orchestrator()

result = orch.run("GOOGL", news_limit=3, stock_days=2)

print("\n=== Collected Data ===")
print(result["collected"])

print("\n=== Analysis ===")
print(result["analysis"])

print("\n=== Memory ===")
print(result["memory"])
