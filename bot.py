import discord
import asyncio
import array
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = '-')

whitelistedUsers = ['Mashhhyyy#7521', 'Example#1234', 'WhitelistedUser#54321']

TOKEN = 'BOT_TOKEN_HERE'

@bot.event
async def on_ready():
    print('Ready!')


@bot.event
async def on_member_join(member):
    if str(member) not in whitelistedUsers:
        await bot.kick(str(member))


bot.run(TOKEN)