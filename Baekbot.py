import discord
import asyncio
import requests
import openpyxl

client = discord.Client()



@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("백랑이랑 메이플")
    await client.change_presence(status=discord.Status.online, activity=game)
    twitch = "baeklang04"
    name = "백랑"
    channel = client.get_channel(726378027746852874)
    a = 0
    while True:
        headers = {'Client ID': '8x2af6dvfblevkm3demrks0120f16l'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a = 0:
                await channel.send(name + "이 방송을 켰는데 한번 가봅시다 고고!")
                a=1
        except:
            a = 0
        await asyncio.sleep(15)




@client.event
async def on_message(message):
    if message.content.startswith("백"):
        await message.channel.send("랑")

    if message.content.startswith("!뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name= "벙어리")
        await author.add_roles(role)


client.run("NzcxMTgzODAyMzUyOTI2ODEw.X5oa4g.dytQzVnIbaBASEw-UQJMV2LlYwE")

