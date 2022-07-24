import discord
from bcolors import bcolors
from command import Command
import requests
import random


class Fish(Command):
    def __init__(self):
        super().__init__('Fish', 35)

    async def execute(self, channel: discord.abc.GuildChannel, retries=0):
        msg: discord.Message = await self.wait_for_response(channel, 'pls fish')
        if msg == None:
            return
        if 'Catch the fish!' in msg.content:
            print(f'{bcolors.OKBLUE} Catching Kraken :O{bcolors.ENDC}')
            emojis = []
            chars = []
            scanning = False
            for char in msg.content:
                if scanning:
                    chars.append(char)
                if char == '<':
                    scanning = True
                if char == '>':
                    scanning = False
                    emojis.append(''.join(chars))
                    if len(emojis) >= 3:
                        break
                    chars = []
            position = 0
            for n, v in enumerate(emojis):
                if emojis.count(v) == 1:
                    position = n
            try:
                # just presses a random button lmao
                id = (await self.get_message_dict(msg))['components'][0]['components'][position]['custom_id']
            except:
                return
            session = self.client.ws.session_id

            data = {
                'type': 3,
                'guild_id': msg.guild.id,
                'channel_id': msg.channel.id,
                'message_id': msg.id,
                'application_id': '270904126974590976',
                'session_id': session,
                'data': {
                    'component_type': 2,
                    'custom_id': id
                }
            }

            header = {
                'authorization': self.client.http.token
            }

            r = requests.post('https://discord.com/api/v9/interactions', json=data, headers=header)
            await self.sendTyping(channel, 'YESSSSSSSS')
        