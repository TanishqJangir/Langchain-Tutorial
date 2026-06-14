from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_classic.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {formate_instructions}",
    input_variables=['feedback'],
    partial_variables={'formate_instructions' : pydantic_parser.get_format_instructions()}
)

classifier_chain = prompt1 | model | pydantic_parser

prompt2 = PromptTemplate(
    template="Write an approprite response to this positive feedback \n {feedback}",
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template="Write an approprite response to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

chain1 = prompt2 | model | parser
chain2 = prompt3 | model | parser

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', chain1),
    (lambda x: x.sentiment == 'negative', chain2),
    RunnableLambda(lambda x: 'could not find sentiment')
)

chain = classifier_chain | branch_chain
result = chain.invoke({'feedback' : 'this is the worst product ever and i want my money back'})
print(result)
chain.get_graph().print_ascii()