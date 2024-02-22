import random
from discord.ext import commands
import discord

class ChoiceCommands(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def rolldice(self,ctx):
    return await ctx.reply(embed = discord.Embed(title = f"🎲: {random.randint(1,6)}",color = discord.Color.from_rgb(255,255,255)))

  @commands.command()
  async def pick(self,ctx,*,options = None):
    options = options.split()
    if options is None:
      return await ctx.reply(embed= discord.Embed(
        title = '🎯 You have not specified options for picking!',
        color = discord.Color.from_rgb(255,255,255)
      ))
    elif options is not None:
      return await ctx.reply(embed = discord.Embed(
        title = f'🏹 I choose: {options[random.randint(0,len(options)-1)]}',
        color = discord.Color.from_rgb(255,255,255)
      ))
    
async def setup(bot):
  await bot.add_cog(ChoiceCommands(bot))

  