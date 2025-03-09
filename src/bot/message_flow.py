from discord import Intents
from discord.ext import commands
from llm.chat import get_response
import re

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
MEMORY = 10
message_history = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if re.search(r'\bex\b', message.content, re.IGNORECASE):
        await message.channel.send('de ex percebo eu eheheh')

    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(name='echo')
async def echo(ctx, *, content: str):
    await ctx.send(content)

@bot.command(name='chat')
async def chat(ctx, *, prompt: str = None):
    if prompt is None:
        await ctx.send("Não escreveste nada seu energúmeno de merda")
    else:
        message_history.append(prompt)

        if len(message_history) > MEMORY:
            message_history.pop(0)

        response = get_response(prompt, message_history)
        await ctx.send(response)

def run(token: str):
    bot.run(token)