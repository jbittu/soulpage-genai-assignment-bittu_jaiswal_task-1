import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory

from agents.data_collector import DataCollectorAgent
from agents.analyst import AnalystAgent

load_dotenv()

class Orchestrator:
    """
    Main controller — collects → analyzes → stores memory.
    """

    def __init__(self):
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        self.collector = DataCollectorAgent()
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("GOOGLE_API_KEY missing in environment variables")

        self.analyst = AnalystAgent(api_key=api_key)

    def run(self, company: str, news_limit=5, stock_days=7):
        # Step 1 — Data collector
        collected = self.collector.collect(company, news_limit, stock_days)
        self.memory.chat_memory.add_user_message(f"Collected: {collected}")

        # Step 2 — Analyst (Gemini LLM)
        analysis = self.analyst.analyze(collected)
        self.memory.chat_memory.add_user_message(f"Analysis: {analysis}")

        return {
            "collected": collected,
            "analysis": analysis,
            "memory": self.memory.load_memory_variables({})
        }


if __name__ == "__main__":
    orch = Orchestrator()
    result = orch.run("Google", 5, 7)
    print(result["analysis"])
