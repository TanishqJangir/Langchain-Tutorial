from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []


while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() == "exit":
        break

    response = model.invoke(user_input)
    chat_history.append(response.content)
    print("Bot: ", response.content)

print("\n\nChat History: ", chat_history)