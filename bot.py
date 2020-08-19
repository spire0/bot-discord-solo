import discord
import dotenv
from codecs import encode
from picselector import menu

dotenv.load_dotenv()

client = discord.Client()
msg_user = msg = bmsg = pedidouser = respostaid = pedidoid = None
start = discord.Embed(title='Escolha seu nsfw da zero two! <:zerogun:738732464117121045>: ',
                      description='**1- Imagens\n 2- Gifs\n 3- Imagens realistas\n 4- Ahegao**\n\n AVISO!!! Não nos responsabilizamos pelo seu pedido<:zerotwocrazy:738974003280216194>',
                      color=1752220)

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


    if message.content.lower() == 'bom dia':  # comando bom dia
        await message.channel.send('bom dia delícia! <:zerotwolove:738974003443662918>')


    if message.content.lower() == '!safadensa':
        if message.channel.is_nsfw():
            global bmsg, pedidouser, pedidoid, respostaid, msg
            bmsg = await message.channel.send(embed=start)
            await bmsg.add_reaction('1️⃣') # tagged
            await bmsg.add_reaction('2️⃣') # gif
            await bmsg.add_reaction('3️⃣') # realista
            await bmsg.add_reaction('4️⃣') # ahegao

            pedidouser = message.author
            pedidoid = message.id
            respostaid = bmsg.id
            msg = message
        else:
            await message.channel.send(content='Esse chat NÃO é nsfw! <:dissapointment:738974002944409642>')
    
    if message.content.lower() == 'eduardo':
        await message.channel.send(content='**E D U A R D O**\n https://cdn.discordapp.com/attachments/497062752473317397/736651644468723842/eduardo_1.mp4', )


@client.event
async def on_reaction_add(reaction, user):

    if user != client.user: # se não for o bot
        if user == pedidouser: # se for o dono do request da msg
            if respostaid == reaction.message.id: # se ele reagiu a msg certa
                await menu(reaction.emoji[0], msg)
                await bmsg.delete()


client.run('MzM5MDg5MDkyMDUyNjQ3OTM2.WXYnUw.LHtk5kKBG3LbF1YlcSTFL1sf5Gk')
