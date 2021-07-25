import os
import discord
from dotenv import load_dotenv

config = load_dotenv()

TOKEN = os.getenv('TOKEN')

from discord.ext import commands
from VoiceRoom import roomObj

# roomObj.createTable()
# roomObj.insert(1, 868611009290579999)
rooms = roomObj.getUserRoomsByUserId(1)

# for item in rooms:
#     ACCESS_ROOMS
#     print(item[2])

ACCESS_ROOMS = [
    868611009290579999,
    863521886888394762
]

client = commands.Bot(command_prefix='$')


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


# @bot.command()
# async def test(ctx):
#     print(ctx)
#     print('inst')
#     createVoiceRoom()
#     return

@client.command()
async def install():
    roomObj.createTable()
    return

@client.command()
async def addVoiceRoom(ctx):
    print(ctx.message.content)
    # Add Validation
    roomObj.createTable()
    return


# client.boadd_command(test)

client.run(TOKEN, bot=True)


# client.run(TOKEN)

# @client.event
# async def on_ready():
#     Channel = client.get_channel('YOUR_CHANNEL_ID')
#     Text= "YOUR_MESSAGE_HERE"
#     Moji = await client.send_message(Channel, Text)
#     await client.add_reaction(Moji, emoji='🏃')
# @client.event
# async def on_reaction_add(reaction, user):
#     Channel = client.get_channel('YOUR_CHANNEL_ID')
#     if reaction.message.channel.id != Channel
#     return
#     if reaction.emoji == "🏃":
#       Role = discord.utils.get(user.server.roles, name="YOUR_ROLE_NAME_HERE")
#       await client.add_roles(user, Role)

# @client.event
# async def on_message(message):
#     guild = message.guild
# channel = await guild.create_voice_channel('cool-channel')
# time.sleep(10)
# await channel.delete()
# if message.author == client.user:
#     return

# guild = ctx.message.guild
# if message.content.startswith('$hello'):
# await message.channel.send('Hello!')
# await discord.VoiceChannel.delete(868611009290579999)

# server = ctx.message.server
# perms = discord.Permissions(send_messages=False, read_messages=True)
# await client.create_role(server, name='NoSend', permissions=perms)


# @client.event
# async def on_reaction_add(reaction, user):
#   ChID = '487165969903517696'
#   if reaction.message.channel.id != ChID:
#     return
#   if reaction.emoji == "🏃":
#     CSGO = discord.utils.get(user.server.roles, name="CSGO_P")
#     await client.add_roles(user, CSGO)
