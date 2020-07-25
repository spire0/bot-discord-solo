const Discord = require('discord.js');
var opcao = 0
var opcao2 = 0

const bot = new Discord.Client();

const senha = 'isso aq vai ficar fora do codigo msm';

bot.login(senha)
bot.on('ready',  () => {
    console.log('O bot está online!')
})

bot.on('message', kamehameha => {
    if (kamehameha.content === 'kamekameha') {
        msg.reply('https://i.pinimg.com/originals/a0/93/d1/a093d193fc2bf97db4e5da6ddda19668.gif') 
    }
})

bot.on('message', msg => {
    if (msg.content === '!safadensa') { 
        msg.reply('```BEM-VINDO A MAIOR LOJA DE SAFADENSA DO BRASIL!\n\ Aqui estão suas escolhas:\n\ 1- Porn\n\ 2- Hentai(Novos lançamentos! E latência de server alta)\n\ 3- Furry (Acesso somente para o Zarakiando)\n\  AVISO! Não nos responsabilizamos pelo seu pedido!```')
        opcao = 1
        bot.on('message', resp => {
            if (opcao === 1) { 
                while (resp.author.id != msg.author.id) {
                    print('Erro! id incorreto/ wait()')
                }
                if (resp.author.id === msg.author.id) {
                    if (resp.content === '1') {
                        resp.channel.send('**Em manutenção!**')
                    }    
                    if (resp.content === '2') {
                        resp.channel.send('```:scroll: ESCOLHA SEU HENTAO! :scroll:\n\ Aqui estão suas escolhas:\n\ 1- Mikasa\n\ 2- Zero Two\n\ 3- Sakura\n\ 4- Jojo reference(Fora de estoque)\n\ 5- Rakudai kishi no cavalery(só os old lembra porra)\n\ 6- Ichigo\n\ 7- Kokoro ```')   
                    }
                    if (resp.content === '3'); {
                        resp.channel.send('**vc eh doente, cara vai se tratar! :rage:**')
                    }
                }               
            }     
        })
        }
    })   

bot.on('message', bodia => {
    if (bodia.content === 'bom dia') {
        bodia.reply('bom dia delicia!')
    }
})
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
