from discord.ext import commands
import discord


class Help(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def help(self, ctx):
    embed = discord.Embed(
      title = '❕HELP',
      description = """**# General Commands**\n🚨 `$help`:**Helps you!**
      💻 `$ping`:**Shows the bot's real time ping in ms**\n👤`$GetUser`:**Shows detailed information about the mentioned user**\n\n**# Webscraping**
    🤖 `$chat`:**Ask ChatGPT anything! Syntax: $chat {your input}**
        🌐 `$wiki`:**Look up any information from Wikipedia! Syntax:$wiki {query}**
        🏯`$reddit_browse`:**Sends a random post from the subreddit of your choice! Syntax $reddit_browse
        {subreddit} (do not include r/)**
        🐸 `$meme`:**Sends a random meme from  r/dankmemes**
        🌦️ `$get_weather`:**Gets the temperature, humidity, etc. of any state of the users choice! Syntax: $get_weather {state}**
        📺`$YouTube`:**Scrapes YouTube and sends back the most relevant result depending on your query. Syntax: $YouTube {query}**\n\n# Random Pickers\n\n
        🎲`$rolldice`:**Rolls a virtual dice landing anywhere from 1-6!**
        🍕`$pick`:**Picks one option from choices the user gives! Syntax: 
        $pick {choice 1} {choice 2}**\n**# Music Commands**
        💿`$play`:**Plays your favourite music from YouTube. Syntax: $play {song_name}**
        ⏸️`$pause`: **Pauses the ongoing song/audio in the voice channel played **
        ▶️`$resume`: **Resumes the paused song/audio in the voice channel played**
        🔊`$sound_effect`: **Plays a sound effect from our 
        assortment of a wide variety of sounds suitable for everyone.**""",
      color = discord.Color.from_rgb(255,255,255)
    )
    await ctx.reply(embed=embed)


async def setup(bot):
  await bot.add_cog(Help(bot))
