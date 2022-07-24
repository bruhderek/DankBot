from threading import Thread
import traceback
import discord
from bcolors import bcolors

from command import Command
import time
import asyncio
import random
from commands.bal import Bal

from commands.beg import Beg
from commands.daily import Daily
from commands.dig import Dig
from commands.fish import Fish
from commands.fishingrod import Fishingrod
from commands.hunt import Hunt
from commands.lifesaver import Lifesaver
from commands.monthly import Monthly
from commands.postmeme import Postmeme
from commands.rifle import Rifle
from commands.search import Search
from commands.shovel import Shovel

channelid = 0
with open('channel.txt', 'r') as channel:
    channelid = int(channel.read())
print('Starting bot...')
client = discord.Client()

commands: list[Command] = [Bal(), Lifesaver(), Rifle(), Fishingrod(), Shovel(), Postmeme(), Search(), Beg(), Daily(), Monthly(), Fish(), Hunt(), Dig()]

@client.event
async def on_ready():
    print(f'Bot is ready. We have logged in as {client.user.display_name}')
    await client.wait_until_ready()
    while True:
        await update()


async def update():
    channel = client.get_channel(channelid)
    for command in commands:
        if time.time() - command.lastExecuted > command.cooldown:
            try:
                command.client = client
                await asyncio.sleep(random.random() * 5)

                print(f'{bcolors.OKGREEN} Executing command {bcolors.OKBLUE}{command.name}{bcolors.ENDC}')
                await command.execute(channel)
                command.lastExecuted = time.time()
                if random.random() < 0.1:
                    await channel.send(random.choice(['Just playin dank memer lol', 'GRINDING DANK MEMER', 'bob the builder is awesome', 'I have so many coins lol']))
                    await asyncio.sleep(random.random() * 5)
                    if random.random() < 0.1:
                        await channel.send(random.choice(['I\'ll take a break', 'IM TIRED LOL', 'Trying to sleep', 'Im sleepin byeeee', 'bruh imma play Virtual Gamer instead', 'Ill take a break bruhhhh', 'it\'s HOMEWORK TIME']))
                        await asyncio.sleep(random.random() * 30 * 60)
            except:
                print(f'{bcolors.FAIL} Error occured while executing command {command.name}, ignoring...\n{traceback.format_exc()}{bcolors.ENDC}')
            

with open('token.txt', 'r') as file:
    token = file.read()
client.run(token, bot=False)