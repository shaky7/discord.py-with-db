import mysql.connector
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
prefix = "."
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)
token = "MTA3MzQyMjc1OTE4NDU2ODQzMQ.GOkpli.xVxp7yiJiI3j4HVcZjt7XF8X4o4t3Uc2lLsYFM"

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='',
  database='gl'
)

cursor = mydb.cursor(dictionary=True)

@bot.event
async def on_ready():
  print("Online")

@bot.command()
async def set(ctx):
sql = "INSERT INTO usuarios (ID, BALANCE) VALUES (%s, %s)"
val = (ctx.author,id, "50")
cursor.execute(sql, val)

@bot.command()
async def bal(ctx):
cursor.execute(f"SELECT BALANCE from usuarios where ID = {ctx.author.id}")

rows = cursor.fetchall()
for row in rows:
  await ctx.send(row["BALANCE"])

bot.run(token)
