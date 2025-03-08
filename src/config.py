import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DISCORD_BOT_TOKEN : str = os.environ.get('DISCORD_BOT_TOKEN')
    OPENAI_API_KEY : str = os.environ.get('OPENAI_API_KEY')
    OPEN_ROUTER_API_KEY : str = os.environ.get('OPEN_ROUTER_API_KEY')
    GROQ_API_KEY : str = os.environ.get('GROQ_API_KEY')

def get_settings() -> Config:
    return Config()
