import asyncio
import discord


# Tutorial class to create list.

# TODO: Find a way to embed a YouTube Playlist (also maybe pretty up the dropdown menu)
class Tutorials(discord.ui.View):
    @discord.ui.select(
        placeholder="Select a module",
        min_values=1,
        max_values=1,
        options=[
            discord.SelectOption(
                label="CO1105",
                description="Object Oriented Programming"
            ),
            discord.SelectOption(
                label="CO1106",
                description="Requirements Engineering"
            ),
            discord.SelectOption(
                label="CO1107",
                description="Advanced Programming and Algorithms"
            ),
            discord.SelectOption(
                label="CO1108",
                description="Foundations of Computation"
            )
        ]
    )
    async def on_select(self, select, interaction):
        embed = discord.Embed(title=f"Tutorial for {select.values[0]}", description="Here are some helpful tutorials for this module", color=discord.Color.random())
        if select.values[0] == "CO1105":
            embed.set_image(url="https://cdn.freebiesupply.com/logos/large/2x/java-logo-png-transparent.png")
            embed.add_field(name="Java",value="WIP, Come back later!", inline=True)
        elif select.values[0] == "CO1106":
            embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Git_icon.svg/2048px-Git_icon.svg.png")
            embed.add_field(name="Git",value="[Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)", inline=True)
        elif select.values[0] == "CO1107":
            embed.set_image(url="https://cdn.freebiesupply.com/logos/large/2x/python-5-logo-png-transparent.png")
            embed.add_field(name="Week 2", value="[Playlist](https://www.youtube.com/playlist?list=PLeVt6bfkArKciyZXBQB4v48Z2ccA7L3El)", inline=True)
            embed.add_field(name="Week 3", value="[Playlist](https://www.youtube.com/playlist?list=PLeVt6bfkArKdRvReeiigILJWhfepMHt6H)", inline=True)
            embed.add_field(name="Week 4", value="[Video](https://youtu.be/m1Fjdnj_Mds)", inline=True)
            embed.add_field(name="Week 5", value="[Playlist](https://www.youtube.com/playlist?list=PLeVt6bfkArKcKV42o5N8ITcGxnPCjCHdH)", inline=True)
            embed.add_field(name="Week 6", value="[Video](https://youtu.be/JlMyYuY1aXU)", inline=True)
        else:
            embed.set_image(url="https://cms-media.bartleby.com/wp-content/uploads/sites/2/2021/05/31175359/Theoretical-Computer-Science-1-1024x389.jpg")
            embed.add_field(name="Theory",value="WIP, Come back later!", inline=True)
        embed.set_footer(text="Bot created by: kaeini")
        await interaction.response.send_message(embed=embed)


async def tutorials(ctx):
    await ctx.defer()
    message = await ctx.send("", view=Tutorials())
    await ctx.followup.send("‎", delete_after=0.1)
    await asyncio.sleep(15)
    await message.delete()



