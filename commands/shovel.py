import random
import discord
from command import Command
import asyncio


class Shovel(Command):
    def __init__(self):
        super().__init__('Shovel', 35 * 50)

    async def execute(self, channel: discord.abc.GuildChannel, retries=0):
        msg = await self.wait_for_response(channel, 'pls item shovel')
        if msg == None:
            return
        if '(0 owned)' in (await self.get_embed_dict(msg))['title']:
            await self.sendTyping(channel, random.choice(['Time to get some shovels', 'oh no i run out of shovel', 'bruh i= nned']))
            await asyncio.sleep(random.random() * 2)
            await self.wait_for_response(channel, 'pls buy shovel')
        else:
            await asyncio.sleep(random.random())
            await channel.send(random.choice(['im ready to fish lol', 'ok Lol', 'i got enough shovel']))