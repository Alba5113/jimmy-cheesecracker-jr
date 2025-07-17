import discord
from discord.ext import commands
import random

helloMessages = ["hi", "hello", "yo", "howdy"]

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        if message.content.startswith('!hello'):
            await message.reply(f'{random.choice(helloMessages)} {message.author.mention}')

        if message.content.startswith('!repeat'):
            splitmessage = message.content.split()
            
            for i in range(int(splitmessage[-1])):
                await message.channel.send(" ".join(splitmessage[1:-1]))

        if message.content.startswith('!choose'):
            options = message.content.split()
            await message.reply(random.choice(options[1:]))
    else:
        await message.reply(message)

client.run('MTM5NTMxMTc1NDgzMzMwMTUwNA.GKTWID.croUk7zDD52YI32gKgzezV3ZVZABzk0K7f43nA')