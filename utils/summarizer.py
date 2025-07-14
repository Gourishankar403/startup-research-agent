from langchain_groq import ChatGroq

from langchain.chains import LLMChain
from dotenv import load_dotenv
from prompts.templates import pdf_summary_template
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama3-8b-8192",
    temperature=0.3
)

summarizer_chain=LLMChain(llm=llm, prompt=pdf_summary_template)

def summarize_text(text:str)->str:
    if not text.strip():
        return "No content to summarize."
    try:
        return summarizer_chain.run(text=text[:4000])
    except Exception as e:
        return f"Error summarizing text: {str(e)}"
