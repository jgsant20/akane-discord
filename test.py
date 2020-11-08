from discord.ext import commands
import discord
import os
import json
import random
import requests
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {'keywords': 'lolis', 'limit':20, 'no_download':True}
print(response.download(arguments))
