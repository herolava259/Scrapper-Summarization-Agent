from bots.utils.get_api_key_json import get_api_key
from tavily import TavilyClient
from typing import List

def search_urls_new_with_topic(topic: str, max_results: int = 6) -> List[str]:
    try:
        api_key = get_api_key('tavily')
        tavily_client = TavilyClient(api_key=api_key)
        prompt = f'What is today\'s {topic} news and updates?'
        response = tavily_client.search(query=prompt, topic="news", max_results=max_results)
        return [result['url'] for result in response['results']]
    except Exception as ex:
        print(f"retuning previous results due to exception reaching tavily\n.{ex}")
        return ['https://apnews.com/politics', 'https://www.politico.com/politics', 'https://www.usatoday.com/news/politics/', 'https://www.cbsnews.com/politics/', 'https://abcnews.go.com/politics', 'https://www.nbcnews.com/politics']


#print(search_urls_new_with_topic('technology'))