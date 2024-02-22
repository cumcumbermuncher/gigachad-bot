from discord.ext import commands
import discord
import urllib.request
import re

class YouTubeFetcher(commands.Cog):
    def __init__(self,bot):
        self.bot = bot 

    @commands.command()
    async def YouTube(self,ctx,*,query = None):
        if query is None:
            return await ctx.reply(embed = discord.Embed(
                title = '🔍 You have not given a search query!',
                color= discord.Color.from_rgb(255,255,255)
            ))
        
        elif query is not None:
            query = query.replace(" ","-")
            search_keyword=query
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            return await ctx.reply("https://www.youtube.com/watch?v=" + video_ids[0])
        
async def setup(bot):
    await bot.add_cog(YouTubeFetcher(bot))
    