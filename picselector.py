import discord
import os
from random import choice

prepath = 'C:\\Users\\xxxxx\\Desktop\\Meu curso em Python\\scripts pv\\bot discord\\images\\'
escolha = None
tupla = ('tagged', 'gif', 'realism', 'ahegao')

### menu ###
async def menu(msgg, reacao):
    await msgg.edit(embed=discord.Embed(title='Pedido entregue<:zerotwolove:738974003443662918>',
                    description=None,
                    color=10038562))
    global escolha
    escolha = tupla[int(reacao)-1]

    with open('./images/' + escolha + '/' + choice(os.listdir(prepath + escolha)), 'wb') as image:
        await msgg.edit(embed=discord.Embed(description=image))

    # await msgg.remove_reaction()