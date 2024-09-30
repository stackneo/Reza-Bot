import asyncio
import discord


# Tutorial class to create list.
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
                description="Python Programming & Algorithms"
            ),
            discord.SelectOption(
                label="CO1108",
                description="Foundations of Computation"
            ),

            discord.SelectOption(
                label="CO2102",
                description="Databases & Domain Modelling"
            )
        ]
    )
    async def on_select(self, select, interaction):
        embed = discord.Embed(title=f"Tutorial for {select.values[0]}", description="Here are some helpful tutorials/materials for this module", color=discord.Color.random())
        if select.values[0] == "CO1105":
            embed.set_image(url="https://cdn.freebiesupply.com/logos/large/2x/java-logo-png-transparent.png")
            embed.add_field(name="Java Basics",value="[Link](https://www.codecademy.com/learn/java-introduction)", inline=True)
            embed.add_field(name="Introduction to OOP",value="[Link](https://www.codecademy.com/learn/learn-java-object-oriented-programming)", inline=True)
            embed.add_field(name="Inheritance & Polymorphism",value="[Link](https://www.codecademy.com/learn/learn-java-classes-and-methods)", inline=True)
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
        elif select.values[0] == "CO2102":
            embed.set_image(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Sql_data_base_with_logo.png/640px-Sql_data_base_with_logo.png")
            embed.add_field(name="Week 1", value="[Playlist](https://www.youtube.com/playlist?list=PLeVt6bfkArKcDa27fwSMqOb7_LnAMeAOI)")
        else:
            embed.set_image(url="https://cms-media.bartleby.com/wp-content/uploads/sites/2/2021/05/31175359/Theoretical-Computer-Science-1-1024x389.jpg")
            embed.add_field(name="Theory",value="WIP! If you find any resources that would be helpful. Please reach out!", inline=True)
        embed.set_footer(text="Bot created by: kaeini")
        #Workaround for the DM function failing occasionally.
        await interaction.response.defer()
        user = interaction.user
        #Sends user embed
        await user.send(embed=embed)
        #Lets user know embed has sent.
        await interaction.followup.send(f"The material for {select.values[0]} has been DM'd to you {interaction.user.name}")


async def tutorials(ctx):
    try:
        await ctx.defer()
        message = await ctx.send("", view=Tutorials())
        await ctx.followup.send("‎", delete_after=0.001)
        await asyncio.sleep(15)
        await message.delete()
    except discord.NotFound:
        print("No tutorials found")


