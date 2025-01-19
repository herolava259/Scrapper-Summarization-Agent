from scraping_web import scrape_web_info
from search_topic import search_urls_with_topic
from extract_data import extract_data


tech_urls = search_urls_with_topic('technology')

information = scrape_web_info(tech_urls[0])

#print(str(information.body)[:50000])
print(extract_data(soup=information))


