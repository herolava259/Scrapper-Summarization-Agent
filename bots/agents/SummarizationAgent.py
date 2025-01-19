from bots.agents.TopicRetriever import TopicRetriever as Retriever
from typing import List, Dict
from bots.models.RetrievedText import RetrievedText
from bots.models.SystemMessage import SummarizerRole
from bots.utils.get_api_key_json import get_api_key
import openai

from openai import OpenAI

class SummarizationAgent:
    def __init__(self, system: str = SummarizerRole):
        self.system_msg = {'role': "system", "content": system}
        self.messages: List[Dict[str, str]] = []
        self.retriever: Retriever = Retriever()
        self.temperature: float = 0.7
        self.max_tokens: int = 256
        if system:
            self.messages.append(self.system_msg)

        openai.api_key = get_api_key('open_ai')
        self.llm: OpenAI =OpenAI(api_key=openai.api_key)

    def __call__(self, message: str):

        def loop_summary(data: List[RetrievedText])-> Dict[str, str]:
            print(data[0].content)
            result_dict: Dict[str, str] = {}
            for d in data:
                if len(self.messages) > 100:
                    self.push_earliest_messages_to_sql_lite()
                self.messages.append({'role': "user", "content": d.content})
                result: str = self.execute()
                result_dict[d.topic] = result
                self.messages.append({'role': 'summarizer', 'content': result})
            print(result_dict)
            return result_dict
        retrieved_data = self.retriever(message)
        return loop_summary(retrieved_data)
    def push_earliest_messages_to_sql_lite(self):
        self.messages.pop(1)
    def execute(self) -> str:

        completion = self.llm.chat.completions.create(model='gpt-4o-mini',
                                                      temperature=self.temperature,
                                                      messages=[self.messages[0], self.messages[-1]],
                                                      max_tokens=self.max_tokens)

        return completion.choices[0].message.content

    def get_messages(self) -> List[Dict[str, str]]:
        return self.messages

    def justify_temperature(self, temp: float):
        self.temperature = temp

    def justify_max_tokens(self, max_tok: int):
        self.max_tokens = max_tok


# summarizer = SummarizationAgent()
#
# res = summarizer("can you tell me about Barack Obama")
#
# print(res)
