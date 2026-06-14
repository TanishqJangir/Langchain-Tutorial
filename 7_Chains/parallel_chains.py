from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()
model2 = ChatOpenAI()


prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short questions and answers from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n {notes} and {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chains = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

final_chain = parallel_chains | prompt3 | model1 | parser

text = """
SpaceX is an American aerospace manufacturer and space transportation services company founded by Elon Musk. It was founded in 2002 to reduce space transportation costs and enable the colonization of Mars. SpaceX has since developed the Falcon 9 rocket and the Dragon spacecraft, which are used to transport cargo and astronauts to the International Space Station.

SpaceX is also developing the Starlink satellite constellation, which will provide high-speed internet access to underserved areas around the world. The company is also working on the Starship, a fully reusable rocket that will be used to transport cargo and astronauts to Mars.

The company has achieved many milestones in the space industry, including the first private company to launch, orbit, and recover a spacecraft, the first private company to send a spacecraft to the International Space Station, and the first private company to send a spacecraft to Mars. SpaceX is also the first company to develop a fully reusable rocket, which has significantly reduced the cost of space transportation.
"""
    
result = final_chain.invoke({'text' : text})
print(result)

final_chain.get_graph().print_ascii()