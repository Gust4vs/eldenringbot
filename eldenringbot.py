import random
import os
from discord.ext import commands

bot=commands.Bot(command_prefix='!')

trigger_words=['elden', 'ring', 'elden ring']

responses = [
    'OOOOHHH ELDEN RING!',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Portrait_photoshoot_at_Worldcon_75%2C_Helsinki%2C_before'
    '_the_Hugo_Awards_%E2%80%93_George_R._R._Martin.jpg/1024px-Portrait_photoshoot_at_Worldcon_75%2C_Helsinki%2C_before'
    '_the_Hugo_Awards_%E2%80%93_George_R._R._Martin.jpg',
    'Forged by two brilliant icons, #ELDENRING will transport players into a dark fantasy world created by '
    'Hidetaka Miyazaki (Dark Souls) and George R. R. Martin (A Song of Ice and Fire).',
    'https://preview.redd.it/g5cqloucguw51.png?width=720&auto=webp&s=0455b92b4c1ff884f27a5e273e55f06ccb2a30fb',
    'https://i.redd.it/2cscbuoqkex51.png',
    'https://preview.redd.it/n4hy3z6yz0y51.png?width=720&auto=webp&s=218f85357995aa8b40d67d83cdb66acdfa107dac',
    'https://preview.redd.it/i8drzu2vp4651.png?width=743&auto=webp&s=a3568d1d28d633c7d836a83077386d153dd627aa',
    'https://i.redd.it/ikagnlo8uqd51.gif',
    'https://preview.redd.it/ykig491zvjj51.jpg?width=633&auto=webp&s=db8ad22daddb6e4e3441b0014965a83e83add576',
    'https://preview.redd.it/xrwxo7mphcw51.png?width=585&auto=webp&s=7b58bd46b6df1bf47cd5f8689165f85a251975b0',
]

@bot.event
async def on_ready():
    print(bot.user.name)
    print(bot.user.id)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # Check if any words in the message have a trigger word in them
    for word in message.content.lower().split(' '):
        if word in trigger_words:
            # Send a random response if a trigger word is found
            await message.channel.send(random.choice(responses))
            # Break here to avoid sending multiple messages if someone writes multiple trigger words at once
            break

bot.run(os.environ.get('elden_token'))

