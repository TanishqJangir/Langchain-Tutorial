from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list."]
    summary : Annotated[str, "Summary of the review"]
    sentiment : Annotated[str, "Sentiment of the review : Positive,Negative,Neutral"]
    rating : Annotated[float, "Rating of the review : 1-5"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside the list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside the list"]
    name: Annotated[Optional[str], "Name of the reviewer"]
    
structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 rocessor makes everything lightning fast—whether I'm gaming, multitasking, or asts a full dav even with heavv use. and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 20MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to leex actually works well for distant objects, but anything beyond loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,30 price tag is also a hard pill to swallow.

pros :
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons :
Bulky and heavy—not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors
""")

print(result)