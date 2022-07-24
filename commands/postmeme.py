import discord
import requests
from command import Command
import random


class Postmeme(Command):
    def __init__(self):
        super().__init__('Postmeme', 40)

    async def execute(self, channel: discord.abc.GuildChannel):
        msg: discord.Message = await self.wait_for_response(channel, 'pls pm')
        try:
            id = (await self.get_message_dict(msg))['components'][0]['components'][random.randint(0, 4)]['custom_id']
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
