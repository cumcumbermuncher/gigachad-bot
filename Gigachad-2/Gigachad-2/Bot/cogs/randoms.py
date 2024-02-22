
from discord.ext import commands 
import discord

class RandomCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def developers(self,ctx):
        embed = discord.Embed(
            title='👔 Our Fabulous Team',
            description="""
                **💼 Chief Technical Officer: `Ishan`**\n
                **🎨 Chief Design Officer: `Aarnav`**\n
                **👨‍💻 Chief Architect:** `Aahan`\n
            """,
            color = discord.Color.from_rgb(255,255,255)

        )
        await ctx.reply(embed = embed)

    @commands.command()
    async def invite(self,ctx):
        embed = discord.Embed(
            title='📬 Invite me to your server!',
            description="""
                **🖱️ Click Here and add me to your server for better utility!**
            """,
            url="https://discord.com/oauth2/authorize?client_id=1121804393474437203&permissions=2684798976&scope=bot",
            color = discord.Color.from_rgb(255,255,255)

        )
        await ctx.reply(embed = embed)

async def setup(bot):
    await bot.add_cog(RandomCommands(bot))