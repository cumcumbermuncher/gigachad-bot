from discord.ext import commands
import discord
import openai

class chat(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    openai.api_key = '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'
  
  @commands.command()
  async def chat(self,ctx,*,query = None):
    try:
      if query is None:
        await ctx.reply(embed = discord.Embed(
          title = '❗ No Query Specified',
          description = '**🤖 Use the command in the following way `$chat your_query`**',
          color=discord.Color.from_rgb(255, 255, 255)))
      elif query is not None:
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          temperature=0,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0,
          messages=([{"role": "user", "content": query}])
        )
        await ctx.reply(embed = discord.Embed(
          title = '🤖 ChatGPT Response',
          description = response['choices'][0]['message']['content'],
          color=discord.Color.from_rgb(255, 255, 255)))
    except:
      await ctx.reply(embed = discord.Embed(
          title = '🤖 Looks like you have been sending too many requests. This has resulted in a temporary rate limit. ')
      )
async def setup(bot):
  await bot.add_cog(chat(bot))
