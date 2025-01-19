from typing import List, Dict
from duckduckgo_search import DDGS

def search_urls_with_topic(topic: str, max_results: int = 6) -> List[str]:
    try:
        ddg = DDGS()
        prompt = f'What is today\'s {topic} news and updates?'
        results: List[Dict[str, str]] = ddg.text(topic, max_results=max_results)
        return [i["href"] for i in results]
    except Exception as e:
        print(f"returning previous results due to exception reaching ddg.")
        return ['https://apnews.com/politics', 'https://www.politico.com/politics', 'https://www.usatoday.com/news/politics/', 'https://www.cbsnews.com/politics/', 'https://abcnews.go.com/politics', 'https://www.nbcnews.com/politics']



# query = 'technology'
#
# print(search_url_with_topic(query))