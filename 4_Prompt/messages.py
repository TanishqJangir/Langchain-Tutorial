from langchain_core.messages import content
from langchain_core.outputs import chat_result
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content='Tell me about Langchain')
]


result = model.invoke(messages)

messages.append(AIMessage(content=result.content))


print(messages)