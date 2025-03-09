from langchain.agents import tool
from typing import List, Dict
from bots.scrapers.tavily_search_urls import search_urls_new_with_topic
from bots.scrapers.scraping_web import scrape_web_info
from bots.scrapers.extract_data import extract_data
from pydantic import BaseModel, Field

class ScrapingDataInput(BaseModel):
    '''retrieve data from key topic that the user say with tool name's scrape_data'''
    topics: List[str] = Field(..., description='The topics that the user want to known. For example sport, technology, political')

@tool(args_schema=ScrapingDataInput)
def scrape_data(topics: List[str]) -> Dict[str, List[str]]:
    """scrape data follow by topic (likes sport, technology, political,...vv) from internet"""

    urls_gr_by_topic: Dict[str, List[str]] = {topic: search_urls_new_with_topic(topic, max_results=6) for topic in topics}

    return {topic : [extract_data(scrape_web_info(url)) for url in urls] for topic, urls in urls_gr_by_topic.items()}



