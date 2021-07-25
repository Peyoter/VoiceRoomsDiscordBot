import discord
import sqlite3
from discord.ext import commands

from config import *

client = discord.Client()
bot = commands.Bot(command_prefix='!')

createdChannelList = dict()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_voice_state_update(member, before, after):
    channelName = 'Канал ' + str(member.nick)

    if after.channel is not None and member.id in createdChannelList:
        if after.channel.id != createdChannelList[member.id].id:
            await createdChannelList[member.id].delete()
            createdChannelList.pop(member.id)

    if after.channel is not None and after.channel.id in ACCESS_ROOMS:
        channel = await member.guild.create_voice_channel(channelName, overwrites=None, category=after.channel.category)
        await member.move_to(channel)
        await channel.set_permissions(member, manage_channels=True)
        createdChannelList[member.id] = channel
        return

    if after.channel is None and before.channel is not None:
        if createdChannelList[member.id]:
            await createdChannelList[member.id].delete()
            createdChannelList.pop(member.id)
        return


client.run(TOKEN)