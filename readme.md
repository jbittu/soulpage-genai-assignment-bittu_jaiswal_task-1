#  Company Intelligence Agentic System

A multi-agent AI system built using **LangChain**, **Google Gemini 2.0 Flash**, **NewsAPI**, **Alpha Vantage**, and **Streamlit**.  
This application gathers real-time company information—including news & stock performance—and generates intelligent insights, risks, and summaries through LLM-based reasoning.

##  Core Features

###  Multi-Agent Architecture

| Agent | Responsibility |
|-------|----------------|
| **Data Collector Agent** | Fetches real-time company news & stock market data |
| **Analyst Agent (Gemini 2.5)** | Summarizes data, finds risks, trends, recommendations |
| **Orchestrator Agent** | Coordinates agents, maintains memory using LangChain |


###  Streamlit Web Interface
- Enter **company name / ticker symbol (AAPL, GOOG, TATASTEEL, etc.)**
- Fetch **Live Market News + Stock Trend Charts**
- Generate **AI Reasoning Outputs**
- Conversation memory retained across queries
- Useful for **Analysts, Investors, Businesses & Research teams**



##  System Architecture

```bash
            ┌───────────────────┐
            │     User Input    │
            └─────────┬─────────┘
                      │
                      ▼
            ┌───────────────────┐
            │   Orchestrator    │
            │ (Controller Agent)│
            └─────────┬─────────┘
    ┌─────────────────┼──────────────────┐
    ▼                 ▼                  ▼
┌──────────────┐ ┌────────────────┐ ┌────────────────────┐
│Data Collector│ │ Analyst Agent  │ │ Conversation Memory│
│  (Agent 1)   │ │    (Gemini)    │ │ (LangChain Buffer) │
└───────┬──────┘ └────────┬───────┘ └──────────┬─────────┘
        │                 │                    │
        ▼                 ▼                    ▼
 Real News (NewsAPI)  LLM Insights      Maintains Context
 Real Stocks (AV API) Summary & Risks   Across Sessions
```

##  Project Structure

```bash
soulpage-genai-assignment-bittu_jaiswal_task-1/
│── agents/
│   ├── data_collector.py
│   └── analyst.py
│
│── tools/
│   └── fetchers.py
│
│── orchestrator.py
│── streamlit_app.py
│── test_news.py
│── test_stock.py
│── test_orchestrator.py
│── requirements.txt
│── .env
│── README.md
```


##  Installation & Setup

###  Clone the repository

```bash
git clone https://github.com/jbittu/soulpage-genai-assignment-bittu_jaiswal_task-1.git
cd soulpage-genai-assignment-bittu_jaiswal_task-1
```

###  Create virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate         # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```


##  API Keys (Environment Variables)

Create **.env** file in project root:

```bash
GOOGLE_API_KEY=your_gemini_api_key
NEWSAPI_KEY=your_newsapi_key
ALPHA_VANTAGE_KEY=your_alpha_vantage_key
```

- Get Keys:


| Service | Link |
|--------|------|
| Gemini | https://aistudio.google.com/app/apikey |
| NewsAPI | https://newsapi.org/ |
| Alpha Vantage | https://www.alphavantage.co/ |


##  Testing Backend Agents

```bash
python test_news.py          # Fetch live news
python test_stock.py         # Get stock prices
python test_orchestrator.py  # Full agent pipeline
```

---

##  Run Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

## Example Usage

### Query Example
Input:
```
Company: Microsoft (MSFT)
```

✔ Retrieves latest 10 global news headlines  
✔ Fetches 7-day historical stock closing prices  
✔ AI generates analysis:

```
 Stock Trend → Upward momentum detected last 4 days  
 News Sentiment → Mostly positive  
 Risks → AI Divestment concerns, antitrust investigations in EU  
 Investment Decision → Moderate Buy
```



## Final Output Preview

| Output Section | Description |
|---------------|-------------|
|  Live Market News | Company headlines + timestamps + sources |
|  Stock Trend Plot | Closing price curve using Alpha Vantage |
|  Strategic Insights | Market positioning, opportunities |
|  Risk Assessment | Financial, legal, geopolitical threats |
|  Recommendation | Buy / Hold / Sell (LLM supported reasoning) |

##  Credits

Built with:

- LangChain
- Google Gemini 2.0 Flash
- Streamlit
- NewsAPI
- Alpha Vantage


