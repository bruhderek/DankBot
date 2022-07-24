import discord
from command import Command


class Daily(Command):
    def __init__(self):
        super().__init__('Daily', 24 * 3600)

    async def execute(self, channel: discord.abc.GuildChannel):
        await self.wait_for_response(channel, 'pls daily')
