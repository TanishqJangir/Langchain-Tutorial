from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="9_RAG/Document_Loader/employees.csv")

docs = loader.load()

print(docs)
print(docs[0].page_content)