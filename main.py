import mysql.connector
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
prefix = ""
bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)
token = ""

mydb = mysql.connector.connect(
  host='',
  user='',
  password='',
  database=''
)

cursor = mydb.cursor(dictionary=True)

@bot.event
async def on_ready():
  print("Online")

@bot.command()
async def set(ctx):
sql = "INSERT INTO "" ("", "") VALUES (%s, %s)"
val = (ctx.author,id, "50")
cursor.execute(sql, val)

@bot.command()
async def bal(ctx):
cursor.execute(f"SELECT "" from "" where "" = {ctx.author.id}")

rows = cursor.fetchall()
for row in rows:
  await ctx.send(row[""])

bot.run(token)
