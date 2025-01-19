from bots.tools.scrape_data import scrape_data
from bots.tools.search_wikipedia import search_wikipedia
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
import openai
from bots.utils.get_api_key_json import get_api_key
from bots.prompts.KeyReceiverPrompt import key_receiver_prompt

# from langchain.schema.output_parser import StrOutputParser



def build_summarization_flow():
    tools = [scrape_data, search_wikipedia]
    functions = [convert_to_openai_function(f) for f in tools]
    #print(functions)
    api_key = get_api_key('open_ai')
    openai.api_key = api_key
    extract_key_model = ChatOpenAI(model = 'gpt-3.5-turbo-1106', api_key=api_key, temperature = 0).bind(functions=functions)
    questions_prompt = ChatPromptTemplate.from_messages([
        ('system', key_receiver_prompt),
        ("user", "{input}")
    ])

    chain = questions_prompt | extract_key_model | OpenAIFunctionsAgentOutputParser()

    return chain

# simp_chain = build_summarization_flow()
# result = simp_chain.invoke({"input": "Elon Musk"})
# print(result)
#