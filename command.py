import traceback
import discord
from discord.ext import commands
import random
import asyncio
import requests
import json

from bcolors import bcolors

class MessageNotFoundError(BaseException):
        pass

class Command:
    name = ''
    cooldown = 0
    client: discord.Client = None
    def __init__(self, name: str, cooldown: int):
        self.name = name
        self.cooldown = cooldown
        self.lastExecuted = 0

    async def execute(self, channel: discord.abc.GuildChannel):
        return

    async def sendTyping(self, channel: discord.abc.GuildChannel, text: str):
        async with channel.typing():
            await asyncio.sleep(random.random() / 2)
        await channel.send(text)

    async def wait_for_response(self, channel: discord.abc.GuildChannel, message: str, retries=0):
        if retries > 5:
            print(f'{bcolors.FAIL} No response while executing command {bcolors.OKBLUE}{self.name}{bcolors.ENDC}')
            await self.sendTyping(channel, random.choice(['BRUH WHY IS THIS NOT WORKIN', 'BRUH WHY IS THIS NOT WORKING', 'dude wtf is dank memer down', 'bruh', 'ahhhhhhhhhhhhh', 'why is it not working uwu']))
            if random.random() < 0.3:
                await self.sendTyping(channel, random.choice(['Is dank memer down', 'DANK MEMER IS DOWN UGGH', 'Dank memer? wtf', 'wtf', 'DANK MEMER SUCKS BRUH']))
            return
        await self.sendTyping(channel, message)
        def check(m: discord.Message):
            return m.channel == channel and m.author.display_name == 'Dank Memer'
        try:
            msg = await self.client.wait_for('message', check=check, timeout=10)
            return msg
        except Exception as e:
            print(f'{bcolors.WARNING} No response while executing command {bcolors.OKBLUE}{self.name}{bcolors.WARNING}, retrying... (Error: {e}){bcolors.ENDC}')
            await asyncio.sleep(random.random() * 2)
            await self.wait_for_response(channel, message, retries=retries+1)

    async def get_message_dict(self, msg: discord.Message):
        with open('token.txt', 'r') as file:
            token = file.read()
        header = {
            'authorization': token
        }
        with open('channel.txt', 'r') as channel:
            channelid = int(channel.read())
        r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=header)
        for message in json.loads(r.text):
            if int(message['id']) == int(msg.id):
                return message
        raise MessageNotFoundError()

    async def get_embed_dict(self, msg: discord.Message):
        return (await self.get_message_dict(msg))['embeds'][0]

