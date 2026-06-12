from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

json_schema_review = {
    "title" : "Review",
    "type" : "object",
    "properties" : {
        "key_themes" : {
            "type" : "array",
            "items" : {
                "type" : "string"
            },
            "description" : "Write down all the key themes discussed in the review in a list."
        },
        "summary" : {
            "type" : "string",
            "description" : "Summary of the review"
        },
        "sentiment" : {
            "type" : "string",
            "enum" : ["Positive", "Negative", "Neutral"],
            "description" : "return sentiment of the review : Positive,Negative,Neutral"
        },
        "rating" : {
            "type" : "number",
            "description" : "Rating of the review : 1-5"
        },
        "pros" : {
            "type" : ["array", "null"],
            "items" : {
                "type" : "string"
            },
            "description" : "Write down all the pros inside a list."
        },
        "cons" : {
            "type" : ["array", "null"],
            "items" : {
                "type" : "string"
            },
            "description" : "Write down all the cons inside a list."
        },
        "name" : {
            "type" : ["string", "null"],
            "description" : "Name of the reviewer"
        }
    },
    "required" : ["key_frames", "summary", "sentiment", "rating"]
}

structured_model = model.with_structured_output(json_schema_review)
result = structured_model.invoke("""
    I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 rocessor makes everything lightning fast—whether I'm gaming, multitasking, or asts a full dav even with heavv use. and the 45W fast charging is a lifesaver.

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