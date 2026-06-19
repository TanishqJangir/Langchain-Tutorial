from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {joke}',
    input_variables=['joke']
)

passthrough = RunnablePassthrough()

parser = StrOutputParser()

chain1 = RunnableSequence(prompt1, model, parser)
chain2 = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explaination' : RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(chain1, chain2)

result = final_chain.invoke({'topic' : 'AI'})

print(result)