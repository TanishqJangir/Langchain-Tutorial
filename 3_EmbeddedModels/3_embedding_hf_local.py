from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Delhi is the capital of india",
    "Jaipur is the capital of Rajasthan",
    "Paris is the capital of France",
    "London is the capital of UK"
]

result = embedding.embed_documents(documents)
print(str(result))