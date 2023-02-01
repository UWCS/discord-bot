import logging

import discord
from discord.ext import commands
from settings import Settings

# bots need the message content intent to read messages
# https://discordpy.readthedocs.io/en/stable/intents.html
intents = discord.Intents.default()
intents.message_content = True

# create our bot
bot = commands.Bot(command_prefix="!", intents=intents)

# register some callbacks and commands


@bot.event
async def on_ready():
    """This callback is triggered when the bot is ready"""
    logging.info(f"Logged in as {bot.user}")
    logging.info(str(bot.user))


@bot.command()  # type: ignore
async def ping(ctx: commands.Context):
    """A simple command to ping the bot and check if it's working."""
    await ctx.reply("Pong!")


@bot.command()  # type: ignore
async def hello(ctx: commands.Context):
    """Say hello, the bot will say hello back!"""
    await ctx.reply(f"Hello, {ctx.author.name}, my name is {Settings().name}!")
