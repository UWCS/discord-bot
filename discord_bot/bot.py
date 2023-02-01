import logging

import discord
from discord.ext import commands
from settings import Settings

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """This function is called by the bot when it has finished loading and is ready"""
    logging.info(f"Logged in as {bot.user}")
    logging.info(str(bot.user))


@bot.command()
async def ping(ctx: commands.Context):
    """A simple command to ping the bot and check if it's working."""
    await ctx.reply("Pong!")


@bot.command()
async def hello(ctx: commands.Context):
    """Say hello, the bot will say hello back!"""
    await ctx.reply(f"Hello, {ctx.author.name}, my name is {Settings.name}!")
