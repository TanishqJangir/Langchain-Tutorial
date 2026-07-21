from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("9_RAG/Document_Loader/resume.pdf")

docs = loader.load()

print(docs)

print(docs[0].page_content)
print(docs[1].page_content)