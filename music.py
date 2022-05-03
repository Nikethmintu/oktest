import discord
from discord.ext import commands
import youtube_dl

class music(commands.cog):
  def __init__(self, client):
      self.client = client 

def setup(client):
    client.add_cog(music(client)

@commands.command()     
async def join(self,ctx):
       if ctx.author.voice is None:
          await ctx.send("you're not in voice channel")
         
    voice_channel = ctx.author.channel
       if ctx.voice_channel is None
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)
@commands.command
async def disconnect(self,ctx):
    await ctx.voice_client.disconnect()
@commands.command()
async def play (self,ctx,url):
ctx.voice client.stop()
FFMPEG_OPTIONS = {'before_options': '-'-reconnect 1 -reconnect_streamed -reconnect_delay_max 5', 'options': '-vn'}
YDL_OPTIONS={"format":"bestaudio"}
vc= ctx.voice client
with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
     info = ydl.extract_info(url, download=False)

url2 = info['formats'][0]['url']
source = await discord.FFmpeg0pusAudio

@commands.command()
async def pause(self,ctx):
await ctx.voice client.pause()
await ctx.send("Paused )
               
@commands.command()
async def resume(self,ctx):
await ctx.voice client.resume() await 
await ctx.send("resume")


def setup(client):
    client.add_cog(music(client))