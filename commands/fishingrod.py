import random
import discord
from command import Command
import asyncio


class Fishingrod(Command):
    def __init__(self):
        super().__init__('Fishingrod', 35 * 50)

    async def execute(self, channel: discord.abc.GuildChannel, retries=0):
        msg = await self.wait_for_response(channel, 'pls item fishingrod')
        if msg == None:
            return
        if '(0 owned)' in (await self.get_embed_dict(msg))['title']:
            await self.sendTyping(channel, random.choice(['Time to get some rods', 'oh no i run out of rod', 'bruh i= nned rod']))
            await asyncio.sleep(random.random() * 2)
            await self.wait_for_response(channel, 'pls buy fishingrod')
        else:
            await asyncio.sleep(random.random())
            await channel.send(random.choice(['im ready to fish lol', 'ok Lol', 'i got enough rod']))