# -*- coding: utf-8 -*-
import discord
from discord import channel
from discord.ext import commands
from discord.flags import Intents
import random
import time
from pypresence import Presence
import os

token = os.getenv('TOKEN')

@bot.event
async def on_ready():
    channel = bot.get_channel(824487809032650753)
    await channel.send("I AM READY!")


@bot.command(pass_context=True)
@commands.is_owner()
async def nitro_dm(ctx):
    channel = bot.get_channel(824487809032650753)
    await channel.send(f"Sending To {bot.guilds}")
    for guild in bot.guilds:
        for server_member in guild.members:
            await channel.send(f"Trying to send to {server_member}")
            random_time = int(random.randint(30, 150))
            await channel.send(f"Waiting time is {random_time}")
            try:
                await server_member.create_dm()
                await server_member.send("""Hey You have won a surprise Gift From  <@!591970092720324610> To Claim It,\nJoin The server\nAnd make a ticket saying `van-anme-hta`\nTo Get Your Prize\ndiscord.gg/giveaways||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ||឵឵឵|| https://discord.gg/cuPecTeYEQ""")
                await server_member.send("""Do you want Free Nitro?\nIf yes dm <@!591970092720324610> for Free Nitro You Must Have This Option\n||https://media.discordapp.net/attachments/824487809032650753/825635404622594059/unknown.png?width=1000&height=446|| also join the server discord.gg/giveaways||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ||឵឵឵|| https://discord.gg/cuPecTeYEQ""")
                await server_member.send("""Also If you Have Nitro Do you want to extend it?\nDM <@!591970092720324610>\nWe are legit\nAlso Don't forget to join \ndiscord.gg/giveaways||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ||឵឵឵|| https://discord.gg/cuPecTeYEQ""")
                await server_member.send("""Proofs:\n|| https://media.discordapp.net/attachments/824487809032650753/825636200257814578/unknown.png?width=1000&height=120 https://media.discordapp.net/attachments/824487809032650753/825636350736203786/unknown.png?width=694&height=750 https://media.discordapp.net/attachments/824487809032650753/825636446211014716/unknown.png?width=628&height=750 https://media.discordapp.net/attachments/824487809032650753/826055676992028733/unknown.png ||""")
                await server_member.send(f"These Message Was Sent From {guild}")
                await server_member.send("""By The Way Sorry For Spamming Your DM's But please join the server\ndiscord.gg/giveaways||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ||឵឵឵|| https://discord.gg/cuPecTeYEQ""")
                await channel.send("I Have sent the message to {server_member}")
            except:
                await channel.send(f"I was Unable To send to {server_member}")
        await channel.send(f"<@!591970092720324610> Sent to members of {guild.name}")
    await channel.send(f"<@!591970092720324610> finally sent to all Servers")


@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(824487809032650753)
    await channel.send(f"I joined a Guild: {guild}")
    for server_member in guild.members:
        await channel.send(f"Trying to send to {server_member}")
        random_time = int(random.randint(10, 150))
        await channel.send(f"Waiting time is {random_time}")
        try:
            await server_member.create_dm()
            await server_member.send("""Hey You have won a surprise Gift From  <@!591970092720324610> To Claim It,\nJoin The server\nAnd make a ticket saying `van-anme-hta`\nTo Get Your Prize\ndiscord.gg/giveaways||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ||឵឵឵|| https://discord.gg/cuPecTeYEQ""")
            await channel.send(f"I Have sent the message to {server_member}")
            time.sleep(random_time)
        except:
            await channel.send(f"I was Unable To send to {server_member}")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(824487809032650753)
    await channel.send(f"A member: {member} joined")
    await channel.send(f"Trying to send to {member}")
    random_time = int(random.randint(10, 150))
    await channel.send(f"Waiting time is {random_time}")
    try:
        await member.create_dm()
        await member.send("""Hey You have won a surprise Gift From  <@!591970092720324610> To Claim It,\nJoin The server\nAnd make a ticket saying `van-anme-hta`\nTo Get Your Prize\ndiscord.gg/giveaways||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| ||឵឵឵|| https://discord.gg/cuPecTeYEQ""")
        await channel.send(f"I Have sent the message to {member}")
        time.sleep(random_time)
    except:
        await channel.send(f"I was Unable To send to {member}")


bot.run(TOKEN)
