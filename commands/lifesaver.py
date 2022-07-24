import random
import discord
from command import Command
import asyncio


class Lifesaver(Command):
    def __init__(self):
        super().__init__('Lifesaver', 35 * 10)

    async def execute(self, channel: discord.abc.GuildChannel, retries=0):
        msg = await self.wait_for_response(channel, 'pls item lifesaver')
        if msg == None:
            return
        if '(0 owned)' in (await self.get_embed_dict(msg))['title']:
            await self.sendTyping(channel, random.choice(['Time to get some lifesavers', 'oh no i run out of lifesaver', 'bruh i= nned lifesaver']))
            await asyncio.sleep(random.random() * 2)
            await self.wait_for_response(channel, 'pls buy lifesaver')
        else:
            await asyncio.sleep(random.random())
            await channel.send(random.choice(['Lol I already have enough', 'ok Lol', 'i got enough']))