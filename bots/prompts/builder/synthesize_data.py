from bots.models.RetrievedText import RetrievedText
from typing import List

def format_multiple_data_for_the_topic(topic: str, contents: List[str]) -> RetrievedText:

    synthetic_data = '\n'.join([f'*{i}. <source>\n{contents[i]}\n</source>' for i in range(len(contents))])

    return RetrievedText(topic=topic, content = synthetic_data)

