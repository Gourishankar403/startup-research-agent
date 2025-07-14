# agents/research_agent.py

from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq

from data_sources.wiki_loader import fetch_wiki_summary
from data_sources.pdf_loader import extract_text_from_pdf
from utils.summarizer import summarize_text
from data_sources.dummy_api import fetch_dummy_api_data
from dotenv import load_dotenv
import os

# Load Groq API Key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model="llama3-8b-8192",  # ✅ use "model", not "model_name"
    temperature=0.5
)

# Tools used by the agent
tools = [
    Tool(
        name="WikipediaSearch",
        func=lambda query: fetch_wiki_summary(query),
        description="Use this to fetch information about any company, industry, or startup topic from Wikipedia."
    ),
    Tool(
        name="PDFSummarizer",
        func=lambda path: summarize_text(extract_text_from_pdf(path)),
        description="Use this to summarize PDF reports from a given file path."
    ),
    Tool(
        name="StartupTrendsAPI",
        func=lambda query: fetch_dummy_api_data(query),
        description="Simulated tool to get startup trends and investor interest for a topic."
    )
]

# Final prompt for the LLM to give the structured research report
INSIGHTFUL_RESPONSE_PROMPT = """
You are a startup research assistant. Your task is to provide an insightful report on the topic: "{query}".

Respond with the following sections:
1. Overview – explain the topic in simple terms.
2. Latest Trends – 2-3 key innovations or movements in the space.
3. Opportunities – 3 startup or business opportunities.
4. Challenges – major hurdles and pain points.
5. Government Schemes (India) – policies or programs (if applicable).
6. Future Outlook – what’s the long-term potential?
7. Actionable Insight – 2 startup suggestions based on the topic.

Keep it professional, detailed, and specific to the input.
"""

# Initialize the agent with tools
def create_research_agent():
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

# Main query function
def run_research_query(user_query: str) -> str:
    agent = create_research_agent()

    try:
        _ = agent.run(user_query)  # Agent runs tools for exploration (optional)
    except Exception as e:
        print(f"[Agent Tool Error] {e}")

    final_prompt = INSIGHTFUL_RESPONSE_PROMPT.format(query=user_query)
    final_response = llm.invoke(final_prompt)

    # Ensure output is clean text
    return final_response.content.strip()
