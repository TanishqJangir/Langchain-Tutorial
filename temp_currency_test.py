import os
from langchain_core.tools import tool, InjectedToolArg
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from typing import Annotated
import requests

key = os.environ.get("OPENAI_API_KEY")
print("OPENAI_API_KEY present:", bool(key))
llm = ChatOpenAI()

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    url = f"https://v6.exchangerate-api.com/v6/499893dd52e0fccc5d912c39/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rate"]

rate = get_conversion_factor.invoke({"base_currency": "USD", "target_currency": "INR"})
print("rate", rate)

@tool
def convert(base_currency_value: float, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    return base_currency_value * conversion_rate

print(convert.invoke({"base_currency_value": 100, "conversion_rate": rate}))

llm_with_tools = llm.bind_tools([get_conversion_factor, convert])
messages = [HumanMessage("What is the conversion factor between USD and INR? And based on that can you convert 10 usd to inr?")]
ai_message = llm_with_tools.invoke(messages)
print(ai_message)
print(ai_message.tool_calls)
for tool_call in ai_message.tool_calls:
    if tool_call['name'] == 'get_conversion_factor':
        tool_message1 = get_conversion_factor.invoke(tool_call['args'])
        messages.append(tool_message1)
    if tool_call['name'] == 'convert':
        tool_call['args']['conversion_rate'] = tool_message1
        tool_message2 = convert.invoke(tool_call['args'])
        messages.append(tool_message2)
print(messages)
print(llm_with_tools.invoke(messages))
