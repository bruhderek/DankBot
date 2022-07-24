import discord
from command import Command


class Beg(Command):
    def __init__(self):
        super().__init__('Beg', 35)

    async def execute(self, channel: discord.abc.GuildChannel, retries=0):
        await self.wait_for_response(channel, 'pls beg')