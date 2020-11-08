from discord.ext import commands
import discord

class MusicBot(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
