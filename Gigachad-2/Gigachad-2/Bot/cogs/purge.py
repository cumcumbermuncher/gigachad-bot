
from discord.ext import commands
import discord
import asyncio
class clear(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def purge(self,ctx,amount = None):
    await ctx.channel.purge(limit=int(amount))
    embed=discord.Embed(title=f"Successfully purged {amount} messages!",color = discord.Color.from_rgb(255,255,255))
    await asyncio.sleep(1)
    await ctx.send(embed = embed)
    
async def setup(bot):
  await bot.add_cog(clear(bot))