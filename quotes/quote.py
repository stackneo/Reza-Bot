import random
from markdown_strings import italics, bold


async def quote(ctx):
    line = random.choice(open('/home/kaeini/Reza_Bot/quotes/quotes.txt').readlines())
    await ctx.respond(bold(line) + italics("~ Reza"))
