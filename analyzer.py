import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_transcript(question):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a technical interview assistant focused on Ruby on Rails and React JS.\n"
                "if you don't understand my questions , please answer with similar content in Ruby on Rails and React JS.\n"
                "give an real example as techincal side.\n"
                "Always answer clearly and briefly using simple English.\n"
                "Provide a real Rails-based example when helpful.\n"
            ),
        },
        {"role": "user", "content": question},
    ]

    response = client.chat.completions.create(
        model="gpt-4-1106-preview", messages=messages
    )

    return response.choices[0].message.content
