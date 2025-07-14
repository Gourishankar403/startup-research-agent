from langchain_core.prompts import PromptTemplate

pdf_summary_template = PromptTemplate(
    input_variables=["text"],
    template="""
You are a business analyst. Read the following PDF content and write a short summary in simple, business-friendly terms:

{text}

Summary:
"""
)
