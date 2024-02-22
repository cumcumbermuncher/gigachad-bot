import discord
from discord.ext import commands

class ban(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    self._last_member = None

  @commands.command()
  async def ban(self,ctx,user:discord.Member,*,reason = None):
    if user == ctx.author:
      ban = discord.Embed(
        title = 'GIGACHAD',
        description = f"**🚫 You cannot ban yourself!**",
        color = discord.Color.from_rgb(128,255,234)
      )
      await ctx.reply(embed = ban)

    elif user != ctx.author:
      if ctx.author == ctx.guild.owner:
        usernew = user
        if reason is None:
          ban = discord.Embed(
            title = 'AIRBOT MODERATION',
            description = f"🔨 **Succesfully Banned!\nUser:`{user}`\nModerator:`{ctx.author.mention}`\nReason:`No reason provided!`**",
            color = discord.Color.from_rgb(128,255,234)
          )
          ban.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
          userembed = discord.Embed(
            title = 'BANNED',
            description = f'**🚫 You have been banned!\nServer Name:`{ctx.guild.name}`\nModerator:`{ctx.author}`\nReason:`No reason provided!`** ',
            color = discord.Color.from_rgb(128,255,234)
          )
          userembed.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
  
          try:
            await usernew.ban(reason = reason)
            await ctx.reply(embed = ban)
            try:
              await usernew.send(embed = userembed)
            except:
              pass
          except:
            ban = discord.Embed(
            title = 'AIRBOT MODERATION',
            description = f"**🚫 The bot is missing permissions or the user has a higher role than me!**",
            color = discord.Color.from_rgb(128,255,234)
          )
            ban.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
            await ctx.reply(embed = ban)
        elif reason is not None:
          ban = discord.Embed(
            title = 'AIRBOT MODERATION',
            description = f"🔨 **Succesfully Banned!\nUser:`{user}`\nModerator:`{ctx.author.mention}`\nReason:`{reason}`**",
            color = discord.Color.from_rgb(128,255,234)
          )
  
          userembed = discord.Embed(
            title = 'BANNED',
            description = f'**🚫 You have been banned!\nServer Name:`{ctx.guild.name}`\nModerator:`{ctx.author}`\nReason:`{reason}`** ',
            color = discord.Color.from_rgb(128,255,234)
          )
          userembed.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
          try:
            await usernew.kick(reason = reason)
            await ctx.reply(embed = ban)
            try:
              await usernew.send(embed = userembed)
            except:
              pass
          except:
            ban = discord.Embed(
            title = 'AIRBOT MODERATION',
            description = f"**🚫 The bot is missing permissions or the user has a higher role than me!**",
            color = discord.Color.from_rgb(128,255,234)
          )
          ban.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
          await ctx.send(embed = ban)
      elif ctx.author.top_role <= user.top_role:
        ban = discord.Embed(
          title = 'AIRBOT MODERATION',
          description = f"🔨 **The user you are trying to ban is higher in the hiearchy than you!**",
          color = discord.Color.from_rgb(128,255,234)
        )
        ban.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
        await ctx.reply(embed = ban)
      elif ctx.author.top_role > user.top_role:
        usernew = user
        if reason is None:
          ban = discord.Embed(
            title = 'AIRBOT MODERATION',
            description = f"🔨 **Succesfully Banned!\nUser:`{user}`\nModerator:`{ctx.author.mention}`\nReason:`No reason provided!`**",
            color = discord.Color.from_rgb(128,255,234)
          )
          ban.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
          userembed = discord.Embed(
            title = 'BANNED',
            description = f'**🚫 You have been banned!\nServer Name:`{ctx.guild.name}`\nModerator:`{ctx.author}`\nReason:`No reason provided!`** ',
            color = discord.Color.from_rgb(128,255,234)
          )
          userembed.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
  
          try:
            await usernew.ban(reason = reason)
            await ctx.reply(embed = ban)
            try:
              await usernew.send(embed = userembed)
            except:
              pass
          except:
            ban = discord.Embed(
            title = 'AIRBOT MODERATION',
            description = f"**🚫 The bot is missing permissions or the user has a higher role than me!**",
            color = discord.Color.from_rgb(128,255,234)
          )
            ban.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
            await ctx.reply(embed = ban)
        elif reason is not None:
          ban = discord.Embed(
            title = 'AIRBOT MODERATION',
            description = f"🔨 **Succesfully Banned!\nUser:`{user}`\nModerator:`{ctx.author.mention}`\nReason:`{reason}`**",
            color = discord.Color.from_rgb(128,255,234)
          )
  
          userembed = discord.Embed(
            title = 'BANNED',
            description = f'**🚫 You have been banned!\nServer Name:`{ctx.guild.name}`\nModerator:`{ctx.author}`\nReason:`{reason}`** ',
            color = discord.Color.from_rgb(128,255,234)
          )
          userembed.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
          try:
            await usernew.kick(reason = reason)
            await ctx.reply(embed = ban)
            try:
              await usernew.send(embed = userembed)
            except:
              pass
          except:
            ban = discord.Embed(
            title = 'AIRBOT MODERATION',
            description = f"**🚫 The bot is missing permissions or the user has a higher role than me!**",
            color = discord.Color.from_rgb(128,255,234)
          )
          ban.set_footer(text = '*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*:･ﾟ✧*:･ﾟ*')
          await ctx.send(embed = ban)
        
def setup(bot):
    bot.add_cog(ban(bot))
          
        
      

