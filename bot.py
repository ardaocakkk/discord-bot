import discord
import crypto_news
import token_prices
import os


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="hos-geldiniz")
    await channel.send(f"{member} aramıza katıldı. Hoş geldin!")


@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name='ayrilanlar')
    await channel.send(f"{member} aramızdan ayrıldı")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!crypto-news'):
        news = crypto_news.news()
        await message.channel.send(news)

    if message.content.startswith('!bitcoin-data'):
        bitcoin_data = token_prices.bitcoin_data()
        await message.channel.send(bitcoin_data)
    if message.content.startswith('!eth-data'):
        eth_data = token_prices.eth_data()
        await message.channel.send(eth_data)

    if message.content.startswith('!sol-data'):
        sol_data = token_prices.sol_data()
        await message.channel.send(sol_data)

    if message.content.startswith('!bnb-data'):
        bnb_data = token_prices.bnb_data()
        await message.channel.send(bnb_data)

    if message.content.startswith('!ada-data'):
        ada_data = token_prices.ada_data()
        await message.channel.send(ada_data)

    if message.content.startswith('!hot-coins'):
        hot_coins = token_prices.top_five_Coins()
        await message.channel.send(hot_coins)

client.run(os.getenv("DISCORD_TOKEN"))
