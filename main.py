import discord
from discord.ext import commands,tasks

#use any prefix ig

bot = commands.Bot(command_prefix='$')

#when your bot is ready it will do these

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('with your mom'))
    print('We have logged in as {0.user}'.format(bot))

#ping command as a test ig
@bot.command()
async def ping(ctx):
    await ctx.send(f"your ping is {round(bot.latency * 1000)}ms")


target_channel_id = 618230847996166165

#ok in the brakets below you can make it seconds,hours

@tasks.loop(seconds=24)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("sample text")

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("DONE")
    
#and of course the token    
#don't forget this line

called_once_a_day.start()
bot.run()
