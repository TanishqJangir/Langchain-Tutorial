from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template= "Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Generate a linkedin post about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

final_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model, parser),
    'post' : RunnableSequence(prompt2, model, parser)
})

result = final_chain.invoke({'topic' : 'AI'})

print(result)