import streamlit as st
from orchestrator import Orchestrator
from dotenv import load_dotenv
import traceback

load_dotenv()

st.set_page_config(
    page_title="Company Intelligence Agentic System",
    layout="wide"
)

st.title(" Company Intelligence — Multi-Agent System ")
st.write("This app collects real company news + real stock data and analyzes them using your multi-agent system.")

company = st.text_input("Enter Company Name or Stock Symbol (e.g., Google, GOOGL, MSFT)", "GOOGL")

col1, col2 = st.columns(2)
with col1:
    news_limit = st.slider("Number of news articles", 1, 10, 3)
with col2:
    stock_days = st.slider("Stock history days", 3, 30, 7)

if st.button(" Run Analysis"):
    with st.spinner("Running multi-agent system..."):
        try:
            orch = Orchestrator()
            result = orch.run(company, news_limit=news_limit, stock_days=stock_days)

            collected = result["collected"]
            analysis = result["analysis"]
            memory = result["memory"]

            # --- DISPLAY OUTPUTS ---
            st.subheader(" Collected News")
            st.json(collected["news"])

            st.subheader(" Collected Stock Data")
            st.json(collected["stock"])

            st.subheader(" Analysis")
            st.markdown(analysis)

            st.subheader(" Memory")
            st.json(memory)

        except Exception as e:
            st.error("An error occurred while running the agent system.")
            st.code(traceback.format_exc())
