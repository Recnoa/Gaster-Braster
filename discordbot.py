from discord.ext import commands
from os import getenv
import traceback
import discord
token="OTc5ODA4NTE1MDQyNDcyMDQ2.GdDPkk.dLCJjZkEKIc5FkpoP0-ZVzYQtI_tc3psBH-AiQ"

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
  print("起動完了")


@bot.command()
async def a(ctx,target):
    await ctx.send(target)


bot.run(token)
