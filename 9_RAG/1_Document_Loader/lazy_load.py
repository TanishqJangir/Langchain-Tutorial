from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

loader = DirectoryLoader(
    path='books',   #here is the path of the directory
    glob='*.txt',   #here is the glob pattern
    show_progress=True,#to show the progress of the loader
    loader_cls=PyPDFLoader
)


#load the documents
docs = loader.lazy_load()

print(docs)