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