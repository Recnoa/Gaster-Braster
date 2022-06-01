import discord
from discord.ext import commands

TOKEN = "your-token-here"
bot = commands.Bot(command_prefix="!")

#bot起動完了時に実行される処理
@bot.event
async def on_ready():
    print('ログイン成功')

#メッセージ受信時に実行される処理
@bot.event
async def on_message(message):
    #on_messageイベントの取得とコマンド機能を併用する際に必要な処理
    await bot.process_commands(message)
