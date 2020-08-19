import discord
import os
from random import choice

embed = discord.Embed(title='Pedido entregue<:zerotwolove:738974003443662918>',
                      color=10038562,
                      url=None,
                      description=None)
escolha = no_repeating = None
options = ('tagged', 'gif', 'realism', 'ahegao')

async def menu(reacao, mensagem):
    global escolha, random_image, file_path, formato, no_repeating
    
    escolha = options[int(reacao)-1]
    file_path = 'C:/images/' + escolha
    random_image = choice(os.listdir(file_path))
    formato = random_image[len(random_image) - 3:]
    
    while random_image == no_repeating:
        random_image = choice(os.listdir(file_path))
 
    if random_image != no_repeating:
        file = discord.File(file_path + '/' + random_image, filename='geaga.' + formato)
        embed.set_image(url="attachment://geaga." + formato)
        await mensagem.channel.send(file=file, embed=embed)
        no_repeating = random_image
