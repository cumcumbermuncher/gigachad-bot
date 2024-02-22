from discord.ext import commands
import discord

class Ping(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def ping(self,ctx):
    ping_embed = discord.Embed(
      title = '📶 Latency',
      description = f'**PING: `{round(self.bot.latency*1000,2)}ms`**',
      color = discord.Color.from_rgb(255,255,255)
    )
    await ctx.reply(embed=ping_embed)

async def setup(bot):
  await bot.add_cog(Ping(bot))

@commands.command()
async def spam(self,ctx):
    while True:
      await ctx.send("<@" + str(795491630660321291) + ">  You are Such a loser. You have a tiny pp. Get good. Learn how to program")