from langchain import LLMChain, PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

DEFAULT_PROMPT = """
You are a financial analyst.
Analyze the following company data and produce:

1. Executive Summary (3–5 sentences)
2. Key Insights (bullet points)
3. Top 3 Risk Factors
4. Recommended Next Steps

Company: {company}

News:
{news_text}

Stock Summary:
{stock_summary}
"""

class AnalystAgent:
    """
    Agent 2: Takes collected data and produces insights using Gemini.
    """

    def __init__(self, api_key: str, model: str = "gemini-2.0-flash", temperature=0.2):
        self.llm = ChatGoogleGenerativeAI(
            google_api_key=api_key,
            model=model,
            temperature=temperature
        )

        self.prompt = PromptTemplate(
            template=DEFAULT_PROMPT,
            input_variables=["company", "news_text", "stock_summary"]
        )

        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def _format_news(self, news_list):
        lines = []
        for n in news_list:
            lines.append(
                f"- {n['title']} — {n['summary']} (Published: {n['published_at']})"
            )
        return "\n".join(lines)

    def _format_stock(self, stock):
        return (
            f"Latest Close: {stock['latest_close']}\n"
            f"7-Day Change: {stock['7d_change_pct']}%\n"
            f"Prices: {[p['close'] for p in stock['prices']]}"
        )

    def analyze(self, data):
        news_text = self._format_news(data["news"])
        stock_text = self._format_stock(data["stock"])

        return self.chain.run(
            company=data["company"],
            news_text=news_text,
            stock_summary=stock_text
        )
