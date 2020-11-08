from discord.ext import commands
import config
import discord

class PyExecuteCommandService(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def py(self, ctx, *, args):
    if not str(ctx.message.author.id) == config.ADMIN_ID:
      await ctx.send('You\'re not Lyp, get away >:( {}')
      return

    command = args

    try:
      result = eval(command)
      await ctx.send(result)
    except Exception as e:
      await ctx.send('\'{}\': {}'.format(command, e))
