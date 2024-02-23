import discord
from discord.ext import commands
from threading import Thread
import os
import time
import datetime
import psutil

intents = discord.Intents.default()
intents.message_content = True
start_time = time.time()

bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')
@bot.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('https://images-ext-1.discordapp.net/external/J0eC-lZGcxJyq1AVf7lpHSZT7VeEEV2sKHdN1hNunHU/https/media.tenor.com/epNMHGvRyHcAAAPo/gigachad-chad.mp4')
        break
    
async def load(cogs):
  extensions = [
     'cogs.profile',
     'cogs.dice',
     'cogs.help',
     'cogs.youtube',
     'cogs.reddit',
     'cogs.ping',
     'cogs.chat',
     'cogs.sounds',
     'cogs.wiki',
     'cogs.music',
     'cogs.weather',
     'cogs.memes',
     'cogs.purge',
     'cogs.news',
     'cogs.dice',
     'cogs.profile',
     'cogs.randoms'
     ]
  
  for file in os.listdir(cogs):
    for extension in extensions:
      try:
        await bot.load_extension(extension)
      except:
        pass

@bot.event
async def on_ready():
  await load('cogs')
  await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('with balls'))

@bot.command()
async def uptime(ctx):
        current_time = time.time()
        difference = int(round(current_time-start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(title='🗿 Here are my uptime statistics:',colour=discord.Color.from_rgb(255,255,255))
        embed.add_field(name="⌚ Uptime", value=f"{text}")
        embed.add_field(name = '🖥️ Processor Count', value = f'{psutil.cpu_count()}')
        embed.add_field(name='🧠 Virtual Memory', value = f'{psutil.virtual_memory()[2]}gb')
        embed.set_footer(text="chad.io")
        try:
            await ctx.reply(embed=embed)
        except discord.HTTPException:
            await ctx.reply("Current uptime: " + text)

if __name__ == '__main__':
    bot.run('TOKEN')
