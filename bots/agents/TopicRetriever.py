from langchain_core.agents import AgentFinish

from bots.flows.summarization_functions_flow import build_summarization_flow
from typing import List, Dict
from bots.models.RetrievedText import RetrievedText
from bots.tools.scrape_data import scrape_data
from bots.tools.search_wikipedia import search_wikipedia
from bots.prompts.builder.synthesize_data import format_multiple_data_for_the_topic

class TopicRetriever:
    def __init__(self):

        self.chain = build_summarization_flow()
        self.tool_dict = {'scrape_data': scrape_data, 'search_wikipedia': search_wikipedia}

    def __call__(self, message: str):

        print(f'message: \n {message}')
        function_call = self.chain.invoke({"input": message})
        if isinstance(function_call, AgentFinish):
            return [RetrievedText('Unknown', "Can not search key word from your question")]
        if function_call.tool == 'scrape_data':
            #print(function_call)
            retrieved_data: Dict[str, List[str]] = self.tool_dict[function_call.tool].invoke(function_call.tool_input)
            return [format_multiple_data_for_the_topic(topic, contents) for topic, contents in retrieved_data.items()]
        elif function_call.tool == 'search_wikipedia':
            retrieved_data: str = self.tool_dict['search_wikipedia'].invoke(function_call.tool_input)

            return [RetrievedText(function_call.tool_input['query'], retrieved_data)]

        return []


# retriever = TopicRetriever()
#
# print(retriever("Elon Musk")[0].content)
