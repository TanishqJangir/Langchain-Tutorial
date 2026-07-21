from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Write a summary for the following text - \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

loader = TextLoader("9_RAG/Document_Loader/cricket.txt", encoding="utf-8")

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'text' : docs[0].page_content})

print(result)