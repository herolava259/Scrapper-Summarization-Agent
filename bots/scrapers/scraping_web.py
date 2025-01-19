import requests
from bs4 import BeautifulSoup
import re



def scrape_web_info(url: str) -> BeautifulSoup:
    p = re.compile('^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')

    if not p.match(url):
        return None
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return None
            # parse result
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except Exception as ex:
        print(f'Some error when fetching data from {url}.\n Error: {ex}')
        return None


