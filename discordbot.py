from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    @client.event
async def on_message(message):こんにちは
    #bot自身が送信したメッセージには反応しない
    if message.author == client.user:
        return
    await message.channel.send("こんにちは")

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
