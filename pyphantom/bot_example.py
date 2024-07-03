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
    words = message.content.split()
    c_limit = ' '.join(words[2:3])
    try:
        c_limit = int(c_limit)
    except ValueError:
        print("Invalid input for c_limit. Please enter a number.")

    print(c_limit)
    
    if message.author == client.user:
        return

    if message.content == str('super facto del dia'):
        response = ollama.generate(model='llama3', prompt='Provide a proven and accurate random fact in Spanish, under 50 characters, with no additional text.')
        await message.channel.send(response['response'])

client.run('MTI1MzQ3NzI3Njg4NTA2MTgwMw.GLNJEP.3Jcfy8LO_Ln5OASOhfpYE_3lRdR-EL6LfYnqX0')


'''
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

    if client.user.mentioned_in(message):

        words = message.content.split()
        pyphantom_propmt = ' '.join(words[1:])

        response = ollama.generate(model='llama3', prompt=pyphantom_propmt + 'under 100 characters')
        await message.channel.send(response['response'])

client.run('your-token')


'''