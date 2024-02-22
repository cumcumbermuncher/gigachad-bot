import discord
from discord.ext import commands
import time
class AvatarStuff(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def GetUser(self,ctx,member: discord.Member):
    embed = discord.Embed(
      title = f'🔎 Info for {member}',
      color = discord.Color.from_rgb(255,255,255)
    )
    embed.add_field(name = '🪪 User ID',value = member.id)
    embed.set_image(url = member.avatar)
    embed.add_field(name = '🐒 Server Nickname',value = member.nick)
    embed.add_field(name = '🔠 User Name',value = member)
    embed.add_field(name = '📅 Account creation',value = member.created_at.strftime('%Y-%m-%d'))
    return await ctx.reply(embed = embed)



async def setup(bot):
  await bot.add_cog(AvatarStuff(bot))