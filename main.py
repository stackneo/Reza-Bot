import discord
import os
from dotenv import load_dotenv
from quotes.quote import quote
from tutorials import tutorials

load_dotenv()
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready to recieve commands!")


@bot.slash_command(name="quote", description="Generate a wise quote from Reza himself")
async def quote_command(ctx):
    await quote(ctx)


# TODO: Implement tutorial feature.
@bot.slash_command(name="tutorial", description="Link to helpful tutorials related to SEM2 modules")
async def tutorials_command(ctx):
    await tutorials(ctx)


bot.run(os.getenv('TOKEN'))
