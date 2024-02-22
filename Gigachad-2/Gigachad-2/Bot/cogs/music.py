from discord.ext import commands
import discord
import pafy
import urllib.request
import re

class MusicCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        return
    
    @commands.command()
    async def pause(self,ctx):
        vc = ctx.voice_client
        if not vc or not vc.is_playing():
            embed = discord.Embed(title="🎶 I am currently `not` playing anything", color=discord.Color.from_rgb(255,255,255))
            return await ctx.reply(embed=embed)
        elif vc.is_paused():
            embed = discord.Embed(title="🎶 The song is already `paused`!", color=discord.Color.from_rgb(255,255,255))
            return await ctx.reply(embed=embed)

        vc.pause()
        await ctx.reply(embed = discord.Embed(title = '🎧 Paused',color=discord.Color.from_rgb(255,255,255)))
        
    @commands.command()
    async def resume(self,ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_connected():
            embed = discord.Embed(title = "🎶 I'm `not` connected to a voice channel", color=discord.Color.from_rgb(255,255,255))
            return await ctx.reply(embed=embed)
        elif not vc.is_paused():
            embed = discord.Embed(title="🎶 The song is already `resumed`!", color=discord.Color.from_rgb(255,255,255))
            await ctx.reply(embed = embed)
            return

        vc.resume()
        await ctx.reply(embed = discord.Embed(title = '💿 Resumed',color=discord.Color.from_rgb(255,255,255) ))

    @commands.command()
    async def play(self,ctx,*,song = None):
        if song is None:
            return await ctx.reply(embed=discord.Embed(
                title = '💿 You have not given a query for music'
            ))
        try:
            song = song.replace(' ','-')
            search_keyword=song
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            song = "https://www.youtube.com/watch?v=" + video_ids[0]
        except:
            return await ctx.reply(embed = discord.Embed(
                title = '❗ ERROR PLAYING',
                description= '**🔎 Your search query is not on YouTube!**',
                color = discord.Color3.from_rgb(255,255,255)
            ))
        try:
            await ctx.voice_client.stop()
        except:
            pass

        if ctx.author.voice is None:
            await ctx.reply(embed = discord.Embed(title = '❗ ERROR PLAYING',description='📞 **You are `not` in a voice channel!**',color=discord.Color.from_rgb(255,255,255) ))
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()

        video = pafy.new(song)                                                                                                                       
        best = video.getbestaudio()                                                                                                                 
        playurl = best.url
        title = video.title
        duration = video.duration
        thumbnail = video.thumb
        print(thumbnail)                                                                                                                                                                                                                                   
        source = discord.FFmpegPCMAudio(executable = "C:\\Users\\aarna\Downloads\\ffmpeg-2023-09-07-git-9c9f48e7f2-full_build\\ffmpeg-2023-09-07-git-9c9f48e7f2-full_build\\bin\\ffmpeg.exe",source=playurl)
        ctx.voice_client.play(source)
        embed = discord.Embed(
            title = '💿 MUSIC PLAYER',
            description=f'**🎶 Playing: `{title}`\n\n⏱️ Duration:`{duration}`\n\n🎙️ Author:`{video.author}`\n**',
            color=discord.Color.from_rgb(255,255,255)
        )
        embed.set_thumbnail(url = str(thumbnail))
        await ctx.reply(embed = embed)


async def setup(bot):
    await bot.add_cog(MusicCommands(bot))