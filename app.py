from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

model = ChatOpenAI(model='gpt-5-mini')

with open('Financial Chatbot.txt', 'r') as file:
    SYSTEM_PROMPT = file.read()

prompt = ChatPromptTemplate([
    ('system', SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name='history'),
    ('human', '{query}')
])

parser = StrOutputParser()

chain = prompt | model | parser

store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key= 'query',
    history_messages_key='history'
)

st.subheader("🤖 Financial Services Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask your financial question..."):
    response = chatbot.invoke(
        {"query": prompt},
        config={"configurable": {"session_id": "user_1"}}
    )

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        st.write(response)