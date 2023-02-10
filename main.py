import mysql.connector
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
prefix = "!"
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)
token = "MTA3MzQyMjc1OTE4NDU2ODQzMQ.GJkJcR.mr9PbVHgUkLzqr2Y5HS0qQqOec-_YC1I8GVhqI"


@bot.event
async def on_ready():
  print("Online")


bot.run(token)