import re
from bs4 import BeautifulSoup
from typing import List

def extract_data(soup: BeautifulSoup | None) -> str:

    if not soup:
        return ''
    data: List[str] = []

    for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
        txt = tag.get_text(' ', strip=True)
        data.append(txt)

    aggr_txt: str = '\n'.join(data)

    aggr_txt = re.sub(r'\s+', ' ', aggr_txt)

    return aggr_txt[:1000]


