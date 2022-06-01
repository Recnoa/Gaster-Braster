import discord
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
async def on_voice_state_update(member, before, after):
    text_channel = client.get_channel(ID_TEST_CHANNEL)
    #ミュート状態に変化がなければ無視する
    if before.self_mute == after.self_mute:
        return
    if before.self_mute:
        await text_channel.send("{}がマイクミュートを解除しました。".format(member.name))
    else:
        await text_channel.send("{}がマイクをミュートしました。".format(member.name))
    
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
