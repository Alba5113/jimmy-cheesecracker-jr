import discord
from discord.ext import commands
from config import token  # Botun tokenini config dosyasından içe aktarma

import random

intents = discord.Intents.default()
intents.members = True  # Botun kullanıcılarla çalışmasına ve onları banlamasına izin verir
intents.message_content = True

helloMessages = ("howdy", "hi", "hello", "yo")

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')

@bot.command()
async def start(ctx):
    await ctx.send(random.choice(helloMessages))

@bot.command()
async def choose(ctx, *choices):
    await ctx.reply(random.choice(choices[1:]))

@bot.command()
async def repeat(ctx, amount, *phrase):
    phrase = " ".join(phrase)
    for i in range(int(amount)):
        await ctx.send(phrase)

@bot.command()
async def addition(ctx, *nums):
    total = 0

    for j in nums:
        total += int(j)
    await ctx.reply(total)

@bot.command()
async def deduction(ctx, x, *y):
    main = int(x)

    for j in y:
        main -= int(j)
    await ctx.reply(main)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None):
    if member:
        if ctx.author.top_role <= member.top_role:
            await ctx.send("no")
        else:
            await ctx.guild.ban(member)
            await ctx.send(f"banned {member.name}")
    else:
        await ctx.send("wrong format")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("no permissions")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("no user found")
