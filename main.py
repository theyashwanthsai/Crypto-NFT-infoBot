import os
import discord
import crypto_coins_info

my_secret = os.environ['TOKEN']

bot = discord.Client()


@bot.event
async def on_ready():
    print("Logged in {0.user}" .format(bot))
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith("Hello"):
        # print("Hellllllooooo!!!!!!")
      await message.channel.send("Hello!")

    if message.content == "$btc":
      await message.channel.send(crypto_coins_info.message_btc())

    if message.content == "$eth":
      await message.channel.send(crypto_coins_info.message_eth())

    if message.content == "$ada":
      await message.channel.send(crypto_coins_info.message_ada())
      

bot.run(my_secret)
