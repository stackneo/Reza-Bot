import asyncio
import discord


# Tutorial class to create table.

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
        # Outputs a different message depending on the drop down the user selects.
        if select.values[0] == "CO1105":
            await interaction.response.send_message("You selected Object Oriented Programming")
        elif select.values[0] == "CO1106":
            await interaction.response.send_message("You selected Requirements Engineering")
        elif select.values[0] == "CO1107":
            await interaction.response.send_message("You selected Advanced Programming")
        else:
            await interaction.response.send_message("You selected Foundations of Computation")


async def tutorials(ctx):
    await ctx.defer()
    message = await ctx.send("", view=Tutorials())
    await ctx.followup.send("‎", delete_after=0.1)
    await asyncio.sleep(15)
    await message.delete()
