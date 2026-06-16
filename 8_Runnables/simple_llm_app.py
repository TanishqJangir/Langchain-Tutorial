from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Suggest a catchy blog title about {topic}",
    input_variables=["topic"]
)

topic = input("Enter a topic: ")

formatted_prompt = prompt.format(topic=topic)

blog_title = model.invoke(formatted_prompt)
print("Generated Blog Title:", blog_title)