def DiscordLang():
    (write) = print;import discord;from discord.ext import commands;(write('Bot is starting up...'));bot = commands.Bot(command_prefix = '');client = bot;_ = bot;
    @client.event
    async def on_ready():(write('Bot is Online'));
    token = 'NzM0NDAwNTQ2MzI4NDEyMjcx.XxRJzg.mdtGHQOGh8_QnsQy_BFdaGWtPr8';
############################################################################################################################################################################################





    @_.command()
    async def _help(_):
        await _.send('this is the help menu')







    bot.run(token)

