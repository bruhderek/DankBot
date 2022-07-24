import random
import discord
from command import Command
import asyncio


class Rifle(Command):
    def __init__(self):
        super().__init__('Rifle', 35 * 50)

    async def execute(self, channel: discord.abc.GuildChannel, retries=0):
        msg = await self.wait_for_response(channel, 'pls item rifle')
        if msg == None:
            return
        if '(0 owned)' in (await self.get_embed_dict(msg))['title']:
            await self.sendTyping(channel, random.choice(['Time to get some rifles', 'oh no i run out of rifle', 'bruh i= nned rifle']))
            await asyncio.sleep(random.random() * 2)
            await self.wait_for_response(channel, 'pls buy rifle')
        else:
            await asyncio.sleep(random.random())
            await channel.send(random.choice(['im ready to hunt lol', 'ok Lol', 'i got enough rifle']))