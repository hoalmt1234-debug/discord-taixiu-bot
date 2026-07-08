import random
import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} online!")

@bot.command()
async def taixiu(ctx):
    dice = [random.randint(1,6) for _ in range(3)]
    total = sum(dice)

    if total >= 11:
        kq = "🔴 TÀI"
    else:
        kq = "🔵 XỈU"

    await ctx.send(
        f"🎲 {dice}\n"
        f"Tổng: {total}\n"
        f"Kết quả: {kq}"
    )

bot.run(TOKEN)
