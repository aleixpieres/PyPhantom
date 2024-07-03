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
    message = ' '.join(words[1:])
    if message.content == str('summary'):
        c_channel = discord.utils.get(message.guild.text_channels, name='pyphantom')
        messages = [message async for message in c_channel.history(limit=5)]
   
        await message.channel.send(messages.len())
  
client.run('')


