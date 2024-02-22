
from discord.ext import commands
import discord
import random
import asyncpraw as praw
import numpy as np

class RedditBrowser(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def reddit_browse(self,ctx,sub_reddit = None):
        try:
            reddit = praw.Reddit(client_id = 'V21zn8v81BNktj0yINTpyA',
                                client_secret = 'GP3RRVE6xvF-iFQZXWHN64m80Feh9Q',
                                user_agent = 'prawtutorial1v1'
                                )
            await reddit.user.me()
            await reddit.auth.scopes()
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
                        embed = discord.Embed(title=f'__{name}__', colour=discord.Colour.from_rgb(255,255,255), timestamp=ctx.message.created_at, url=url)

                        embed.set_image(url=url)
                        embed.set_footer(text=f"Requested by {ctx.author}")
                        await ctx.reply(embed=embed)
                        break
                    else:
                        pass
        except:
            return await ctx.reply(embed = discord.Embed(title='🍎 There was an error in scraping from reddit',color = discord.Color.from_rgb(255,255,255)))

async def setup(bot):
    await bot.add_cog(RedditBrowser(bot))