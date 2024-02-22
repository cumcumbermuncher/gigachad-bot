import random
import discord
from discord.ext import commands
import asyncpraw as praw
import numpy as np


class Meme(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.reddit = praw.Reddit(client_id = 'V21zn8v81BNktj0yINTpyA',
                             client_secret = 'GP3RRVE6xvF-iFQZXWHN64m80Feh9Q',
                             user_agent = 'prawtutorial1v1'
                             )
    self.sub_reddit = 'dankmemes'
  @commands.command()
  async def meme(self,ctx):
    reddit = self.reddit
    sub_reddit = self.sub_reddit
    await reddit.user.me()
    if sub_reddit is None:
        return await ctx.reply(embed = discord.Embed(
            title='🏮 You have not speficied a sub reddit',
            color= discord.Color.from_rgb(255,255,255)
        ))
    elif sub_reddit is not None:
        subreddit = await reddit.subreddit(sub_reddit)
        all_subs = []
        top = subreddit.hot(limit=100) # bot will choose between the top 250 memes
        all_subs = np.array([])
        async for submission in top:
            all_subs = np.append(all_subs,[submission],axis=0)
        for i in range(0,len(all_subs)):
            random_sub = random.choice(all_subs)
            extension = random_sub.url[len(random_sub.url) - 3 :].lower()
            name = random_sub.title
            url = random_sub.url
            if (extension=='jpg') or (extension=='png') or (extension=='gif'):
                embed = discord.Embed(title=f'__{name}__', colour=discord.Colour.random(), timestamp=ctx.message.created_at, url=url)

                embed.set_image(url=url)
                embed.set_footer(text=f"Requested by {ctx.author}")
                await ctx.reply(embed=embed)
                break
            else:
                pass

async def setup(bot):
  await bot.add_cog(Meme(bot))


