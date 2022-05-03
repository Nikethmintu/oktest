import discord
from discord.ext import commands
import music
import PyNaCl


cogs = [music]
client = commands.Bot(command_prefix='-', intents = discord.Intents.all())


for i in range(len(cogs)):
    cogs[i].setup(client) 




client.run('OTY5MDk4NDg5OTM2MTA1NTcz.YmodTA.uGVif9ln8MLW6E0oJaYC3mmYkqo')