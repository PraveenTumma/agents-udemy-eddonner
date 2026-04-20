import os
from openai import OpenAI
#from openai import AsyncOpenAI
from openai import models
#from openai import OpenAIChatCompletionsModel
from dotenv import load_dotenv
load_dotenv(override=True)


GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")

"""
gemini_client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
#gemini_model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client)


import asyncio

async def main():
	response = await gemini_client.chat.completions.create(model="gemini-2.5-flash-lite", messages=[{"role":"user", "content": "what is 2+2?"}])
	print(response.choices[0].message.content)
	print(response.choices[0].message)

asyncio.run(main())
"""
gemini_client = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
response = gemini_client.chat.completions.create(model="gemini-2.5-flash-lite", messages=[{"role":"user", "content": "what is 2+2?"}])
print(response.choices[0].message.content)
print(response.choices[0].message)
