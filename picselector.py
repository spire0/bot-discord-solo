import discord

from os import path, listdir
from random import choice

valid_options = ('tagged', 'gif', 'realism', 'ahegao')

async def menu(message, reaction):
    option = valid_options[int(reaction) - 1]

    image_path = path.join(__dirname, 'images', option)
    image_random_name = choice(listdir(image_path))
    image_file = discord.File(path.join(image_path, random_image_name))

    message_embed = discord.Embed(
        title='Pedido entregue<:zerotwolove:738974003443662918>',
        description=None,
        color=10038562
    )

    await message.edit(embed=message_embed, file=image_file)
    await message.remove_reaction()
