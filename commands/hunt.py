import discord
from command import Command
import random
import asyncio
from bcolors import bcolors
import requests


class Hunt(Command):
    def __init__(self):
        super().__init__('Hunt', 35)

    async def execute(self, channel: discord.abc.GuildChannel, retries=0):
        msg = await self.wait_for_response(channel, 'pls hunt')
        if msg == None:
            return
        if 'dodge the fireball' in msg.content.lower() or 'dodge the the fireball' in msg.content.lower():
            print(f'{bcolors.OKBLUE} Fighting dragon :O{bcolors.ENDC}')
            await self.sendTyping(channel, random.choice(['EZ dragon', 'OMG DRAGON!??!?!?', 'EPIC', 'epic', 'OMFGGGGGGGGG', 'Bruh OK']))
            try:
                # just presses a random button lmao
                id = (await self.get_message_dict(msg))['components'][0]['components'][random.randint(0, 2)]['custom_id']
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
            await asyncio.sleep(random.random() * 6)
