import wikipedia

def fetch_wiki_summary(query: str) -> str:
    try:
        summary=wikipedia.summary(query, sentences=5)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"⚠️ Your query was ambiguous. Try one of these options: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return "❌ No Wikipedia page found for your query."
    except Exception as e:
        return f"❌ Error fetching Wikipedia data: {str(e)}"
