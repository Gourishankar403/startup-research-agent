import streamlit as st
import textwrap
from agents.research_agent import run_research_query

st.set_page_config(page_title="Startup Research Agent", layout="wide")

# Global dark mode style with white font
st.markdown("""
    <style>
    body, .stApp {
        font-size: 18px !important;
        color: white !important;
        background-color: #0E1117 !important;
    }
    h1, h2, h3, h4 {
        color: white !important;
    }
    .reportview-container .markdown-text-container {
        font-size: 18px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Business Research Assistant")
st.markdown("### 🔍 Enter Your Startup Idea or Research Question")
user_query = st.text_input("E.g. 'AI in education', 'Blockchain for supply chains'")

#pdf_file = st.file_uploader("📄 Upload PDF Report (Optional)", type=["pdf"])

final_report = ""
if st.button("Start Research") and user_query:
    with st.spinner("Researching..."):
        final_report = run_research_query(user_query)

# Display final report
if final_report:
    st.markdown("## 🧠 Final Report", unsafe_allow_html=True)

    clean_report = textwrap.dedent(final_report.strip())
    clean_report = clean_report.replace("**", "")  # Remove all asterisks
    formatted_report = clean_report.replace("\n", "\n\n")
    sections = formatted_report.split("\n\n")

    for section in sections:
        if section.strip():
            lines = section.strip().split("\n")
            if len(lines) > 1:
                header = lines[0]
                body = "\n".join(lines[1:])
            else:
                header = lines[0]
                body = ""

            # White heading and body for dark mode
            st.markdown(f"<h4 style='color:white; font-weight: bold;'>{header}</h4>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:18px; line-height:1.8; color:white;'>{body}</div>", unsafe_allow_html=True)

    # Full report (copyable)
    st.markdown("---")
    with st.expander("📋 View or Copy Full Report"):
        st.code(formatted_report, language="markdown")

    # Download as TXT
    st.markdown("### 📥 Download Report")
    st.download_button(
        label="⬇️ Download as .txt",
        data=formatted_report,
        file_name="business_research_report.txt",
        mime="text/plain"
    )
