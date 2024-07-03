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

    if client.user.mentioned_in(message):

        words = message.content.split()
        c_message = ' '.join(words[1:2])
    

        if c_message == str('summary'):
            pyphantom_propmt = str("Summarize the key points of the next messages:\n")
            c_channel = message.channel
            messages = [message async for message in c_channel.history(limit=10)]
            messages.reverse()
            for message in messages[1:]:
                if message.author != client.user:
                    c_message = f"{message.author}: {message.content}\n"
                    pyphantom_propmt += c_message
                    
            response = ollama.generate(model='llama3', prompt=pyphantom_propmt)
            await message.channel.send(response['response'])
        
        else:
            pyphantom_propmt = ' '.join(words[1:])

            response = ollama.generate(model='llama3', prompt=pyphantom_propmt + 'under 150 characters')
            await message.channel.send(response['response'])


  
client.run('your-token')


