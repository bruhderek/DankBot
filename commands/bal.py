import discord
from command import Command
from bcolors import bcolors


class Bal(Command):
    def __init__(self):
        super().__init__('Bal', 35)

    async def execute(self, channel: discord.abc.GuildChannel, retries=0):
        msg = await self.wait_for_response(channel, 'pls bal')
        if msg == None:
            return
        print(f'{bcolors.OKCYAN} ' + (await self.get_embed_dict(msg))['description'].replace('*', '').replace('`', '').replace('\n', '\n ') + str(bcolors.ENDC))
        