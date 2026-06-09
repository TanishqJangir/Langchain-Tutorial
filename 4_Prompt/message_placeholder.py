import os
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage

# Chat template
chat_templet = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# Load chat history
script_dir = os.path.dirname(os.path.abspath(__file__))
chat_history_path = os.path.join(script_dir, 'chat_history.txt')

chat_history = []
with open(chat_history_path) as f:
    for line in f:
        line = line.strip()
        if line:
            chat_history.append(eval(line))

print("Loaded Chat History:")
print(chat_history)

# Create prompt
prompt = chat_templet.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund?"
})

print("\nRendered Prompt:")
print(prompt)

