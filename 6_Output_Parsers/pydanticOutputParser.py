from sqlalchemy.orm import descriptor_props
from pydantic import Field
from pydantic import BaseModel
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name : str = Field(description="name of the person")
    age : int = Field(gt=18, description="age of the person")
    city : str = Field(description="Name of the city of the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {formate_instructions}",
    input_variables=['place'],
    partial_variables={'formate_instructions' : parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place' : "argentina"})

print(result)


# prompt = template.invoke({"place" : "Indian"})

# print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)
