from discord.ext import commands
# from google import Google
from music import MusicBot
from py_execute_command_service import PyExecuteCommandService
import config
import discord

token = config.TOKEN
bot = commands.Bot(command_prefix='`')

@bot.event
async def on_ready():
  print('Logged on as {0.user}!'.format(bot))

class Greetings(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  @commands.Cog.listener()
  async def on_member_join(self, member):
    channel = member.guild.system_channel
    if channel is not None:
      await channel.send('Welcome {0.mention}.'.format(member))

  @commands.command()
  async def hello(self, ctx, *, member: discord.Member = None):
    member = member or ctx.author
    if self._last_member is None or self._last_member.id != member.id:
      await ctx.send('Hello {0.name}~'.format(member))
    else:
      await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
    self._last_member = member

if __name__ == '__main__':
  bot.add_cog(Greetings(bot))
  # bot.add_cog(Google(bot))
  bot.add_cog(MusicBot(bot))
  bot.add_cog(PyExecuteCommandService(bot))

  bot.run(token)
