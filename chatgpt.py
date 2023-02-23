import openai
import os
from dotenv import load_dotenv
load_dotenv()

token = os.environ.get("API")

openai.api_key = token

model_engine = "text-davinci-003"


def chat_gpt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text
