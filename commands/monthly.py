import discord
from command import Command


class Monthly(Command):
    def __init__(self):
        super().__init__('Monthly', 24 * 3600 * 30)

    async def execute(self, channel: discord.abc.GuildChannel):
        await self.wait_for_response(channel, 'pls monthly')
