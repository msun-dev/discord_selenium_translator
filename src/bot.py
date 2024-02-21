import discord
from discord.ext import commands
from translator import Scraper
from settings_reader import SettingsReader

settings = SettingsReader()

TOKEN = settings.get_value('TOKEN')
channel_to = settings.get_value('channel_to')
channel_from = settings.get_value('channel_from')
admin_id = settings.get_value('admin_id')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# @bot.command()
# @commands.is_owner()
# async def set_channel(context, arg):
#     pass

# @bot.command()
# async def leave(ctx, GID):
#     guild = bot.get_guild(int(GID))
#     await guild.leave()
#     await ctx.send(f"Succesfully left {guild.name}") 

# Add check if message is bot owners one
@bot.event
@commands.guild_only()
async def on_message(ctx):
    if ctx.channel.id != channel_from:
        print('Wrong channel. Return')
        return

    if ctx.author == bot.user:
        print('My own message. Return')
        return

    if ctx.author.id != admin_id:
        print('Message not from admin_id. Retun')
        return
    
    translation = Scraper(str(ctx.content), headless=True).get_translation()
    text = ""
    for i in translation:
        text += i + "\n"

    
    await ctx.add_reaction("\U0001F310")
    specificChannel = bot.get_channel(channel_to)
    await specificChannel.send(text)

bot.run(TOKEN)