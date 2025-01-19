import wikipedia
from langchain.tools import tool
from pydantic import BaseModel, Field

class SearchQueryInput(BaseModel):
    query: str = Field(...,description='The query\'s used for query in Wikipedia')

@tool(args_schema=SearchQueryInput)
def search_wikipedia(query: str) -> str:
    """Run Wikipedia search and get page summaries."""
    page_titles = wikipedia.search(query)
    summaries = []
    for page_title in page_titles[: 3]:
        try:
            wiki_page =  wikipedia.page(title=page_title, auto_suggest=False)
            summaries.append(f"Page: {page_title}\nSummary: {wiki_page.summary}")
        except Exception as ex:
            pass
    if not summaries:
        return "No good Wikipedia Search Result was found"
    return "\n\n".join(summaries)