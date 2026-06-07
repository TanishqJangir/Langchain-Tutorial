from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

documents = [
    "Delhi is the capital of india",
    "Jaipur is the capital of Rajasthan",
    "Paris is the capital of France",
    "London is the capital of UK"
]

result = embedding.embed_documents(documents)

print(str(result)) 