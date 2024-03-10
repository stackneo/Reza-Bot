import random


async def quote(ctx,textfile):
    line = random.choice(textfile)
    text = "~ Reza"
    await ctx.respond(f"**{line}** *{text}*")
