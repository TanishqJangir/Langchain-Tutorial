import os
from dotenv import load_dotenv

# Load environment variables from .env before importing langchain_huggingface.
# This ensures that variables like HF_INFERENCE_ENDPOINT are set in the environment
# before huggingface_hub modules initialize their default endpoints.
load_dotenv()

# Synchronize token environment variables
if "HUGGINGFACEHUB_ACCESS_TOKEN" in os.environ:
    os.environ["HF_TOKEN"] = os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"]
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.environ["HUGGINGFACEHUB_ACCESS_TOKEN"]

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("Write a 5 line poem on Tanishq")
print(result.content)