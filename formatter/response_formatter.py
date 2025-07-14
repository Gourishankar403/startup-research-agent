from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq  # ✅ UPDATED
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama3-8b-8192",
    temperature=0.3
)

formatter_prompt = PromptTemplate.from_template("""
You're a startup analyst assistant.

Using the following raw tool outputs, write a structured research report in Markdown that includes:

- 🧾 Executive Summary
- 📊 Market Trends (as bullet points)
- 💰 VC & Investor Insights
- 🧠 Recommendations

Tool Outputs:
{tool_outputs}
""")

response_chain = LLMChain(llm=llm, prompt=formatter_prompt)

def format_final_output(tool_outputs: str) -> str:
    return response_chain.run(tool_outputs=tool_outputs)
