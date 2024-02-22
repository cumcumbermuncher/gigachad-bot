
from discord.ext import commands
import discord
import aiohttp

class WeatherCommands(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command()
  async def get_weather(self,ctx,*,city = None):
    try:
      url = "http://api.weatherapi.com/v1/current.json"
      params = {
        "key" : '96c552d621464e0e90063018230107',
        "query": city
      }
      async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as res:
          data = await res.json()
       
        location = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]
        condition = data["current"]["condition"]["text"]
      
      embed = discord.Embed(title=f"Weather for `{location}`", description=f"The condition in `{location}` is  `{condition}`",color = discord.Color.from_rgb(255, 255, 255))
      embed.add_field(name=" 🌡️ Temperature", value=f"C: `{temp_c}`")
      embed.add_field(name="💧 Humidity", value=f"`{humidity}%`")
      embed.add_field(name="🎐 Wind speeds", value=f"KPH: `{wind_kph}`")
      
      await ctx.reply(embed=embed)
    except:
      await ctx.reply(embed = discord.Embed(
        title = '🧳 Invalid location provided!',
        color = discord.Color.from_rgb(255,255,255)
      ))

async def setup(bot):
  await bot.add_cog(WeatherCommands(bot))