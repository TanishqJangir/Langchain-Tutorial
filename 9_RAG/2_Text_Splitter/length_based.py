from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('9_RAG\\Text_Splitter\\AI.pdf')

docs = loader.load()


text = """
Snace exploration has Jed to incredlbie scientific discoveres.
From On the Moon to exportng Mars, humanity
continues to push the boundanes of what's possible beyond our
planet.
missions have not expanded our knowledge Of the
universe but have also contributed to advancements in
technology here on Earth. Satellite communications, GPS, and
even certain medical imaging techniques trace the" roots back
to innovations driven by space programs.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(result)