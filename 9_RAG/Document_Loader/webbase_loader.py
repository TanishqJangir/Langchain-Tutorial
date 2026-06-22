from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
prompt = PromptTemplate(
    template='Write a summary for the following text - \n {text}',
    input_variables=['text']
)
parser = StrOutputParser()

chain = prompt | model | parser

url = "https://www.flipkart.com/mania-fashion-graphic-print-superhero-men-round-neck-green-t-shirt/p/itm5f3da4d5c0590?pid=TSHHKEBGZGMKY9C4&lid=LSTTSHHKEBGZGMKY9C43DYZAG&hl_lid=&marketplace=FLIPKART&fm=eyJ3dHAiOiJyZWNvIiwicHJwdCI6ImhwIiwibWlkIjoicGVyc29uYWxpc2VkUmVjb21tZW5kYXRpb24vcDJwLXNhbWUifQ%3D%3D&pageUID=1782150557424"

loader = WebBaseLoader(url)

docs = loader.load()

result = chain.invoke({'text' : docs[0].page_content})

print(result)