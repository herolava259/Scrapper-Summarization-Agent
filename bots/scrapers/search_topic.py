from typing import List, Dict
from duckduckgo_search import DDGS

def search_urls_with_topic(topic: str, max_results: int = 2) -> List[str]:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
        }
        with DDGS(headers=headers) as ddg:
            prompt = f'What is today\'s {topic} news and updates?'
            results: List[Dict[str, str]] = ddg.text(prompt, max_results=max_results)
            print(results)
            return [i["href"] for i in results]


    except Exception as ex:
        print(f"retuning previous results due to exception reaching ddg\n.{ex}")
        return ['https://apnews.com/politics', 'https://www.politico.com/politics', 'https://www.usatoday.com/news/politics/', 'https://www.cbsnews.com/politics/', 'https://abcnews.go.com/politics', 'https://www.nbcnews.com/politics']



# query = 'technology'
#
# print(search_url_with_topic(query))