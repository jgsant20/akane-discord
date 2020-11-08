from discord.ext import commands
import discord
import random
from google_images_download import google_images_download

class Google(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.response = google_images_download.googleimagesdownload()
        
  def _get_image_links(self, image_name):
    arguments = {'keywords': image_name, 'limit':100, 'silent_mode':True, 'no_download':True}
    links = self.response.download(arguments)[0][image_name]
    return links

  @commands.command()
  async def gsearch(self, ctx, *, args):
    image_name = args
    links = self._get_image_links(args)
    link = random.choice(links)

    embed = discord.Embed(
      title=f'\'{image_name}\'  search result',
      url=link)
    embed.set_image(url=link)

    await ctx.send(embed=embed)
