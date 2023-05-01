import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix="!oc", intents = discord.Intents.all())
TOKEN = open("token.txt","r").read()
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
@Bot.command()
async def oguzhancelik(msg):
    await msg.send('en iyisi')

Bot.run(TOKEN)