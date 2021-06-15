import discord
from discord.ext import commands
from utils import tester

class Bot(commands.Bot):
    async def process_commands(self, message):
        
        if message.author.bot and message.author.id != tester.ID:
            return

        ctx = await self.get_context(message)
        await self.invoke(ctx)