from discord.ext import commands
import config
import discord

class PyExecuteCommandService(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  def _parse_commmand(self, command):
    command = "\\n".join(command.splitlines()[1:])

    # strip code block
    if command[-3:] == '```':
      command = command[5:-5]

    command = command.replace('print', 'result.append')

    return command

  @commands.command()
  async def py(self, ctx, *, args):
    if not str(ctx.message.author.id) == config.ADMIN_ID:
      await ctx.send('You\'re not Lyp, get away >:( {}')
      return

    command = self._parse_commmand(args)
    result = []

    try:
      await exec(command)
      await ctx.send(result)
    except Exception as e:
      await ctx.send('\'{}\': {}'.format(command, e))

# def _parse_commmand(command):
#     command = "\\n".join(command.splitlines()[1:])

#     # strip code block
#     if command[-3:] == '```':
#       command = command[5:-5]

#     command = command.replace('print', 'result.append')

#     return command


# y = """
# ```
# for i in range(10):
#   print(x)
# ```
# """

# x = _parse_commmand(y)

# print(x)
