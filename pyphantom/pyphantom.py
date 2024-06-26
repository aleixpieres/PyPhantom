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
