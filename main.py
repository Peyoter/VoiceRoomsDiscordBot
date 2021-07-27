import os
import random
from dotenv import load_dotenv

config = load_dotenv()

TOKEN = os.getenv('TOKEN')

from discord.ext import commands
from VoiceRoom import roomObj

client = commands.Bot(command_prefix='$')
createdChannelList = dict()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_voice_state_update(member, before, after):
    channelName = 'Канал ' + str(member.nick)

    rooms = roomObj.getUserRoomsByUserId(member.id)
    ACCESS_VOICE_ROOMS = []
    for room in rooms:
        ACCESS_VOICE_ROOMS.append(room.discord_room_id)

    # При смене комнаты
    if after.channel is not None and member.id in createdChannelList:
        if after.channel.id != createdChannelList[member.id].id:
            await createdChannelList[member.id].delete()
            createdChannelList.pop(member.id)

    # При входе
    if after.channel is not None and after.channel.id in ACCESS_VOICE_ROOMS:
        channel = await member.guild.create_voice_channel(channelName, overwrites=None, category=after.channel.category)
        await member.move_to(channel)
        await channel.set_permissions(member, manage_channels=True)
        createdChannelList[member.id] = channel
        return

    # При выходе из комнаты
    if after.channel is None and before.channel is not None:
        if member.id in createdChannelList:
            await createdChannelList[member.id].delete()
            createdChannelList.pop(member.id)
        return


@client.command()
async def install(ctx):
    if ctx.guild.owner_id == ctx.author.id:
        roomObj.createTable()
        await ctx.channel.send('Installed!')
    return


@client.command()
async def add(ctx, channel_id):
    channel = client.get_channel(int(channel_id))
    if channel:
        roomObj.insert(int(ctx.author.id), int(ctx.guild.id), int(channel_id))
        await ctx.channel.send(str(channel) + ' - added')
    return


@client.command()
async def remove(ctx, channel_id):
    channel = client.get_channel(int(channel_id))
    if channel:
        roomObj.removeRoom(int(ctx.guild.id), int(channel_id))
        await ctx.channel.send(str(channel) + ' - removed')
    return


@client.command()
async def roll(ctx):
    await ctx.channel.send(str(random.randint(0, 100)))
    return

#
client.run(TOKEN, bot=True)
