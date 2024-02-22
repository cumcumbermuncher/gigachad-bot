import wikipedia
from discord.ext import commands
import discord
import wikipedia

class Wikipedia(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def wiki(self, ctx,*,search=None):
    if search is None:
      embed = discord.Embed(
        title=
        "🌍 `$wikipedia` requires a search query\nFor ex: `$wiki Pablo Escobar`",
        color = discord.Color.from_rgb(255,255,255)
      )
      return await ctx.reply(embed=embed)
    else:
      try:
        data = wikipedia.summary(search)
        title = wikipedia.page(search).title
        embed = discord.Embed(
          title=title,
          description=
          f"{data}",
          color = discord.Color.from_rgb(255,255,255)
        )
        await ctx.reply(embed = embed)
      except:
        embed = discord.Embed(
          title=
          f"🌍 Hmm, looks like what you want to search is not on wikipedia",
          color = discord.Color.from_rgb(255,255,255)
        )
        return await ctx.reply(embed = embed)


async def setup(bot):
  await bot.add_cog(Wikipedia(bot))
