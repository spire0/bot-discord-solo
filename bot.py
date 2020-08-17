import discord
import dotenv
from picselector import menu

dotenv.load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print(f'Bot pronto para o uso em {len(client.guilds)} server(s)')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} server(s)"))



@client.event
async def on_message(message):
                                      # argumentos:
    if message.author == client.user: # para não visualizar a msg dos bots
        return                        #
    if message.channel.name == 'dm':  # para não responder dms
        return                        #


    ### COMANDOS ###
    if message.content.lower() == 'bom dia':  # comando bom dia
        await message.channel.send('bom dia delícia! <:zerotwolove:738974003443662918>')

    if message.content.lower() == '!safadensa':
        global bmsg
        bmsg = await message.channel.send(embed=discord.Embed(title='Escolha seu nsfw da zero two! <:zerogun:738732464117121045>: ',
                                                              description='**1- Imagens\n 2- Gifs\n 3- Imagens realistas\n 4- Ahegao**\n\n AVISO!!! Não nos responsabilizamos pelo seu pedido<:zerotwocrazy:738974003280216194>',
                                                              color=1752220))
        await bmsg.add_reaction('1️⃣') # tagged
        await bmsg.add_reaction('2️⃣') # gif
        await bmsg.add_reaction('3️⃣') # realista
        await bmsg.add_reaction('4️⃣') # ahegao

        global pedidouser
        pedidouser = message.author
        global pedidoid
        pedidoid = message.id
        global respostaid
        respostaid = bmsg.id


@client.event
async def on_reaction_add(reaction, user):

    if user != client.user: # se não for o bot
        if user == pedidouser: # se for o dono do request da msg
            if respostaid == reaction.message.id: # se ele reagiu a msg certa
                await menu(bmsg, reaction.emoji[0])


@client.event
async def on_reaction_remove(reaction, user):
    if user != client.user:
        await bmsg.add_reaction(reaction.emoji) # esquece isso aqui por enquanto, eu ainda n terminei esse pedaço

client.run('hehe')
