from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser\


load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the following joke - {joke}",
    input_variables=['joke']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke('AI')
print(result)