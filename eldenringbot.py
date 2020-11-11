import discord,random
from discord.ext import commands

bot=commands.Bot(command_prefix='!')

trigger_words=['elden', 'ring', 'elden ring'] #add the trigger words to the list

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if any(word.lower() in message.content.lower() for word in trigger_words):
        await message.channel.send('OOOOHHH ELDEN RING!')

bot.run('TOKEN')