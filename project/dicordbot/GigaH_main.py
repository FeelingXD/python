# python discord bot project
import asyncio
import discord

client = discord.Client()
prefix = "기가희재" #접두사

@client.event
async def on_read():
    return
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('기가희재'):
        await message.channel.send('네?')

client.run('NzMwNTc4ODc0ODE1MjE3NzE1.XwbidA.GpPUdzJcAv0L2tiZoGwcKf109Vg')
