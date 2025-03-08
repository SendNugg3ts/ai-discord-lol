from groq import Groq
from jinja2 import Environment, FileSystemLoader
import os
from config import get_settings

env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../prompts')))
template = env.get_template('system_message.jinja2')
system_message = template.render()

def get_response(prompt: str) -> str:
    client = Groq(api_key=get_settings().GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content