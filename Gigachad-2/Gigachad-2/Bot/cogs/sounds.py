
from discord.ext import commands
import discord
import asyncio
from mutagen.mp3 import MP3

class SoundEffects(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command()
  async def sound_effect(self,ctx,*,name = None):
    async def play(url):
      file = 'C:\\Users\\aarna\\Downloads\\Gigachad-2\\Gigachad-2\\Bot\\SoundEffects\\'+url
      audio_source = discord.FFmpegPCMAudio(executable="C:\\Users\\aarna\Downloads\\ffmpeg-2023-09-07-git-9c9f48e7f2-full_build\\ffmpeg-2023-09-07-git-9c9f48e7f2-full_build\\bin\\ffmpeg.exe",source=file)
      ctx.voice_client.play(audio_source)
      duration = MP3(file).info.length
      await asyncio.sleep(float(duration)+1)
      return await ctx.voice_client.disconnect()
    
    if name is None:
      return await ctx.reply(embed = discord.Embed(
        title = '🔊 Sound Effect Assortment',
        description="""📢 Bombard voice channels with a variety of effects in our list.
You can play with:\n`nuclear,
loud indian music,i woke up in a new,
goofy,augh,hacker,galaxy,outro-song,
rizzler,rizzler-2,john-cena,sigma,andrew-tate,
scream,trap,systumm,sus,anthem,bing-chilling`""",
        color = discord.Color.from_rgb(255,255,255)
      ))
    
    if ctx.author.voice is None:
      return await ctx.reply("You are not in a voice channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    name = name.lower()

    if name == 'loud indian music':
      await play('download (1).mp3')
    
    elif 'i woke up' in name:
      await play('download (2).mp3')
    
    elif name == 'augh':
      await play('download.mp3')
    
    elif name == 'goofy':
      await play('download (3).mp3')
    
    elif name == 'nuclear':
      await play('nuclear-fart-1.mp3')
    
    elif name == 'hacker':
      await play('hacker-hai-bhai-hacker-ajjubhai.mp3')
    
    elif name == 'emotional-damage':
      await play('emotional-damage-meme.mp3')

    elif name == 'galaxy':
      await play('galaxy-meme.mp3')

    elif name == 'outro-song':
      await play('outro-song_oqu8zAg.mp3')

    elif name == 'rizzler':
      await play('white-tee-rizz_Pw3bPh4.mp3')

    elif name == 'anthem':
      await play('mahesh_dalle.mp3')
  
    elif name == 'sigma':
      await play('sigma.mp3')

    elif name == 'andrew-tate':
      await play('andrew-tate-theme-song.mp3')

    elif name == 'john-cena':
      await play('and-his-name-is-john-cena-1.mp3')

    elif name == 'rizzler-2':
      await play('the-weeknd-rizzz.mp3')

    elif name == 'scream':
      await play('y2mate_5gbydy1.mp3')

    elif name == 'sus':
      await play('53b1bab6-a8c3-4a1a-82db-7110ce1c29ef_6KNDGWD.mp3')

    elif name== 'trap':
      await play('seeyouagain.mp3')

    elif name == 'putin':
      await play('my-movie-6_0RlWMvM.mp3')

    elif name == 'systumm':
      await play('systumm.mp3')

    elif name == 'bing-chilling':
      await play('bing-chilling.mp3')
    
async def setup(bot):
  await bot.add_cog(SoundEffects(bot))
