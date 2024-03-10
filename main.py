import discord
import os
from dotenv import load_dotenv
from pathlib import Path
from quotes.quote import quote
from tutorials import tutorials
from weather import weather


load_dotenv()
bot = discord.Bot()

#Makes sure textfile is not hardcoded.
current_directory = os.path.dirname(os.path.abspath(__file__))
textfile = open(Path(current_directory) / "quotes" / "quotes.txt").readlines()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready to recieve commands!")


@bot.slash_command(name="quote", description="Generate a wise quote from Reza himself")
async def quote_command(ctx):
    await quote(ctx, textfile)


@bot.slash_command(name="tutorial", description="Link to helpful tutorials related to SEM2 modules")
async def tutorials_command(ctx):
    await tutorials(ctx)

@bot.slash_command(name="weather", description="Pull weather data from your selected city")
async def weather_command(ctx,city):
    await weather(ctx,city)


bot.run(os.getenv('TOKEN'))
