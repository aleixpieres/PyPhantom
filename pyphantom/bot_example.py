# This example requires the 'message_content' intent.

import discord
import ollama

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('super facto del dia'):
        response = ollama.generate(model='llama3', prompt='give me a random fact in spanish under 50 characters, just give me the fact and nothing else')
        await message.channel.send(response['response'])

#client.run('your-token')
