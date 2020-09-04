def DiscordLang():
    (write) = print;import discord;from discord.ext import commands;
    (write('Bot is starting up...'))
    bot = commands.Bot(command_prefix = '')
    client = bot
    _ = bot


    @client.event
    async def on_ready():
        (write('Bot is Online'));

        
    token = 'NzUxMzMxNjI5Mzk3NTczNjYy.X1HiGw.jW4_AtFui26x8NVUPppfTWrsWSU';





    @_.command()
    async def _helpa(_):
        await _.send('this is the help menu')







    bot.run(token)

