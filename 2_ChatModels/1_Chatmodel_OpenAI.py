from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=1.8, max_completion_tokens = 10)
result = model.invoke("Write a 5 line poem on Tanishq")
print(result)
print("\n\n\n", result.content)
