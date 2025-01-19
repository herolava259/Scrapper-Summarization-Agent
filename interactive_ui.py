import streamlit as st
import os
from typing import Dict
from streamlit import session_state
import sys
from bots.agents.SummarizationAgent import SummarizationAgent

def think(agent_bot: SummarizationAgent, msg):
    try:
        summary = agent_bot(msg)
    except Exception as ex:
        summary = 'Some error when summary data'
        pass
    return summary



def simple_synthesize_data(map_data: Dict[str, str]) -> str:
    return '\n'.join([f'Topic:          {key.upper()}\n\n{item}' for key, item in map_data.items()])
# give title to the page
st.title('Summarizer with GPT 4.o mini:')

# initialize session variables at the start once
if 'summarizer' not in st.session_state:
    st.session_state['summarizer'] = SummarizationAgent()

if 'messages' not in st.session_state:
    st.session_state['messages'] = [] #st.session_state['summarizer'].get_messages()[1:]

if 'newly_message' not in st.session_state:
    st.session_state['newly_message'] = ''

# create sidebar to adjust parameters
st.sidebar.title('Model Parameters')
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1)
max_tokens = st.sidebar.slider('Max Tokens', min_value=1, max_value=4096, value=256)

st.session_state['summarizer'].justify_temperature(temperature)
st.session_state['summarizer'].justify_max_tokens(max_tokens)

# update the interface with the previous messages
for message in st.session_state['messages']:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# create the chat interface
if prompt := st.chat_input("Enter your query"):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    # get response from the model
    with st.chat_message('assistant'):
        with st.spinner("Bot's thinking and synthesize..."):
            summarizer = st.session_state['summarizer']
            stream: Dict[str, str] | str = summarizer(prompt)
            response =simple_synthesize_data(stream) if isinstance(stream, dict) else stream
        st.markdown(response)
        st.session_state['messages'].append({"role": "assistant", "content": response})


    # handle message overflow based on the model size