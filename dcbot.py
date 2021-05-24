from discord.ext import commands
import discord
import requests

api_key = ""
bot = commands.Bot(command_prefix = "!b")
@bot.event
async def on_message(message):
    #print(message.content)
    if message.content[0] == "!" and message.content[1] =="b":#to call bot you should use !b for example !b btc_usdt
        
        message.content = message.content[3:]
        #print(message.content)
        if message.author == bot.user or message.author.bot:
             # Ignores if a command is being executed by a bot or by the bot itself
            return
        host = "https://api.gateio.ws/api/v4/spot/tickers?currency_pair={}"#example currency_pair:BTC_USDT or btc_usdt
           
        host1=host.format(message.content)
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        r = requests.request('GET', host1)
        #print(r.json()[0]["last"])
        if r.status_code == 200:
            await message.channel.send(r.json()[0]["last"])
        else:
            await message.channel.send("This pair is not available")

bot.run(api_key)
