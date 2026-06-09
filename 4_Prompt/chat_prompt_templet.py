from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

chat_templet = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', "Explain in simple terms, what is {topic}"),
])

prompt = chat_templet.invoke({
    "domain": "Cricket",
    "topic": "Dusra"
})

print(prompt)