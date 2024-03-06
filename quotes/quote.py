import random
from markdown_strings import italics, bold


async def quote(ctx,textfile):
    line = random.choice(textfile)
    await ctx.respond(bold(line) + italics("~ Reza"))
