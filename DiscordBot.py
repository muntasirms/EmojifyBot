# Work with Python 3.6
import discord
import asyncio
import opus_api
from discord.ext import commands

TOKEN = 'NTAxNTg2MDQyODQzODI0MTQ4.Dqbj5g.IEsBmP02xX7ohUrWtWqHsVmuR94'

client = discord.Client()

def load_opus_lib():
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass


if not discord.opus.is_loaded():
    discord.opus.load_opus()

def emojify(string):

        word = string
        wordArray = []
        totalString = ''
        wordArray = list(word)

        if word != '!end':
            for x in range(0,len(wordArray)):
                if wordArray[x] == '.' or wordArray[x] == ','  or wordArray[x] == '-'or wordArray[x] == '\'' :
                    wordArray[x] = ' '
            for x in range(0, len(wordArray)):
                wordArray[x] = wordArray[x].lower()
                if wordArray[x] == '0':
                    totalString += ':zero: '
                if wordArray[x] == '1':
                    totalString += ':one: '
                if wordArray[x] == '2':
                    totalString += ':two: '
                if wordArray[x] == '3':
                    totalString += ':three: '
                if wordArray[x] == '4':
                    totalString += ':four: '
                if wordArray[x] == '5':
                    totalString += ':five: '
                if wordArray[x] == '6':
                    totalString += ':six: '
                if wordArray[x] == '7':
                    totalString += ':seven: '
                if wordArray[x] == '8':
                    totalString += ':eight: '
                if wordArray[x] == '9':
                    totalString += ':nine: '
                if wordArray[x] == '!':
                    totalString += ':exclamation: '
                if wordArray[x] == '?':
                    totalString += ':question: '
                if wordArray[x] == ';':
                    totalString += ";"
                if wordArray[x] == ' ':
                    totalString += ':black_large_square:' + ' '
                if wordArray[x].isalpha():
                    totalString += ':regional_indicator_' + wordArray[x] + ':' + ' '



        return totalString


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'kill urself {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!emojify'):
        emojifyString = message.content[9:len(message.content)]
        emojifyMsg = emojify(emojifyString)
        if len(emojifyMsg) < 2000:
            msg = emojifyMsg.format(message)
            await client.send_message(message.channel, msg)
        elif len(emojifyMsg) / 2000 > 1:
            wordArray = []
            emojiMsgArr = list(emojifyMsg)
            emojis = 10
            for x in range(0, int(len(emojifyMsg) / 2000) + 1):
                wordArray.append([''])
                for y in range(0, 2000):
                    wordArray[x].append('')
                    # the way the arrays are filled after 2000 are wrong
            for x in range(0, int(len(emojifyMsg) / 2000)):
                for y in range(0, 2000):
                    wordArray[x][y] = emojiMsgArr[(x * 2000) + y]
                    if emojiMsgArr[(x * 2000) + y] == ' ':
                        emojis += 1
                    if emojis > 90:
                        msg2 = ''.join(wordArray[x]).format(message)
                        await client.send_message(message.channel, msg2)
                        emojis = 0
            #for x in range(0, int(len(emojifyMsg) / 2000) ):

                #await client.send_message(message.channel, str(len(emojifyMsg)))
    if message.content.startswith('!mtts on'):

        voice_channel = message.author.voice_channel
        await client.join_voice_channel(voice_channel)

    if message.content.startswith('!mtts off'):
        for x in client.voice_clients:
            if (x.server == message.author.server):
                return await x.disconnect()

    if message.content.startswith('!mtts'):


        #if(client.is_voice_connected(author.message.server)):
        player = voice.create_ffmpeg_player('airplane.mp3')
        player.start()
        #"C:\Users\munta\Desktop" + message.content[5:len(message.content)] + '.mp3'
        #return await client.say("I am not connected to any voice channel on this server!")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print('    ' + server.name)
        await asyncio.sleep(600)
    print('------')



client.run(TOKEN)