import discord
import asyncio
import array
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = '-')

whitelistedUsers = ['Mashhhyyy#7521', 'Example#1234', 'WhitelistedUser#54321']

status = true

TOKEN = 'BOT_TOKEN_HERE'

@bot.event
async def on_ready():
    print('Ready!')


@bot.event
async def on_member_join(member):
    if status:
        if str(member) not in whitelistedUsers:
            await bot.kick(str(member))
    elif !status:
        print('{} joined!'.format(member))
        
@bot.command(pass_context = True)
async def toggle(ctx):
    if status:
        status = False
        await bot.say('Whitelist Toggled Off')
    if !status:
        status = True
        await bot.say('Whitelist Toggled On')
        

bot.run(TOKEN)
