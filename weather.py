import aiohttp
import discord


async def weather(ctx, city):
    api_key = "[YOUR API KEY]"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Makes sure the API request is valid, also sets it to metric so we can get Celsius.
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    # Creates instance of ClientSession to start requests
    async with aiohttp.client.ClientSession() as session:
        # Makes the request using the valid URL
        async with session.get(complete_url) as res:
            # Converts the response from .json to a structure that Oython can parse.
            data = await res.json()
            # Data parsing
            location = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            # m/s is cringe.
            wind_speed = data["wind"]["speed"] * 2.237
            # Converts icon code to valid URL
            icon = f'http://openweathermap.org/img/wn/{data["weather"][0]["icon"]}.png'
            embed = discord.Embed(title=f"Weather for {location}", description=f"Current forecast for {location} is {condition}")
            embed.add_field(name="Temperature", value=f"{temperature}°C")
            embed.add_field(name="Humidity", value=f"{humidity}%")
            embed.add_field(name="Wind Speed", value=f"MPH: {wind_speed:.1f}")
            embed.set_thumbnail(url=icon)
            # Bypass "Application did not respond" error.
            await ctx.defer()
            await ctx.send(embed=embed)
            await ctx.followup.send("‎", delete_after=0.01)
