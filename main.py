import discord
from discord.ext import commands
from discord.ext import tasks
from discord import app_commands

import asyncio
token = "MTEzNTU5Nzg5NTAyMjgxMzIzNA.Gq6lKf.kggVGaRJEA7xImGk5UWk0lYmMprj9QpGQkDmpc"

MY_GUILD = discord.Object(id=746972583877935216)
class MyClient(discord.Client):
  def __init__(self,*,intents:discord.Intents):
    super().__init__(intents=intents)
    self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
      self.tree.copy_global_to(guild=MY_GUILD)
      await self.tree.sync(guild=MY_GUILD)

intent = discord.Intents.default()
intent.message_content = True
intent.members = True
client = MyClient(intents=intent)

"""
@client.event
async def on_message(message):
  if message.content.startswith("hello"):
    time.sleep(5)
#    await message.channel.send("world")

async def on_member_join(member):
  guild = client.guild_get(746972583877935216)
  channel = guild.get_channel(1135251553155022858)
  await channel.send("新規参加者がきたよ")
"""
'''
トリセツ




'''
NEW_ID_ROLE_MEMBER = 1135458219851010088
OLD_ID_ROLE_MEMBER = 1135459869655306343
@client.event
async def on_member_join(member):
    
    welcome_message = f'ようこそ、{member.name}さん！{member.guild.name}へようこそ！'
    channel = member.guild.system_channel
    
    try:
      new_user_role = member.guild.get_role(NEW_ID_ROLE_MEMBER)
      old_user_role = member.guild.get_role(OLD_ID_ROLE_MEMBER)
      await member.add_roles(new_user_role)
      await channel.send(welcome_message)
      await asyncio.sleep(100)
      await member.remove_roles(new_user_role)
      await member.add_roles(old_user_role)

    except:
      await channel.send("error")

@client.tree.command(
  name="test",
  description="testコマンド"
)
@app_commands.describe(test_1="test")
async def test(inter:discord.Interaction,test_1:str):#ロール付与イベントコマンド
#  await inter.response.defer(ephemeral=True)
#  await inter.followup.send_message(test)
  await inter.response.send_message(test_1)

@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if (message.author == user):
        return
    msg = f"{message.author.mention} {reaction}\nFrom:{user.display_name} \
          \nMessage:{message.content}\n{message.jump_url}"
    CHANNEL_ID = 1083366220616704041
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(msg)

@client.event
async def on_message(message):#発言回数、発言内容の取得
   if (message.author == 745967438654603285):
      await message.channel.send("clear")

client.run(token)