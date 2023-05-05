import discord
from discord.ext import commands
from utils import *
from functions import *

Bot = commands.Bot(command_prefix="!ock", intents = discord.Intents.all())
game = Game()
@Bot.event
async def on_ready():
    print("ben hazırım")

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="hoşgeldiniz")
    await channel.send(f"{member} aramıza katıldı hoşgeldi")
    print(f"{member} aramıza katıldı hoşgeldi")

@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gülegüle")
    await channel.send(f"{member} aramızdan ayrıldı :(")
    print(f"{member} aramızdan ayrıldı :(")
@Bot.command(aliases = ["game", "oyun"])
async def ock(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice()) #zar atma
    else:
        await ctx.send('en iyisi')

@Bot.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount) #mesaj silme

@Bot.command(aliases=["copy"])
async def clone_channel(ctx, amount = 1):
    for i in range(amount):
        await ctx.channel.clone() #kanal kopyalama
Bot.run(TOKEN)