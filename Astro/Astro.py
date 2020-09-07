import discord
from discord import Embed
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='^')
client.remove_command('help')

@client.event
async def on_ready():
    print('{0.user} is up and running'.format(client))
    await client.change_presence(activity=discord.Game(name="Astronomical"))

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return

    if message.content.startswith('<@!751447995270168586>'):
        mentionembed = discord.Embed(title="Astro", description="Prefix: `^`\nBot Info: `help` `info`", color=0x7289DA)
        await message.channel.send(embed=mentionembed)

@client.command()
async def info(ctx):

        infoembed = discord.Embed(title="Info", description="**Astro Bot** \nA Utilities Discord Bot with reliability and simplicity\nMade By isirk#0001", color=0x7289DA)
        infoembed.add_field(name= "<a:694943336661778512:731625838398799964> Updates", value="Version 0.9 \n<:status_online:752277014668640296> Finished info, help, ping, kick, ban, avatar, mention, slowmode, clear commands \n<:status_idle:752277014651863070> Making welcome-leave message\n<:status_dnd:752277014345678989> Future things are reaction roles and modlog", inline=True)
        infoembed.add_field(name= ":link: Links", value="[Bot Site](https://asksirk.com/Astro) \n[Github Repository](https://github.com/ISIRK/Astro) \n[Patreon](https://www.patreon.com/Astro_Bot)")
        infoembed.set_footer(text="Astro Bot | discord.gg/7yZqHfG")

        await ctx.send(embed=infoembed)

@client.command()
async def help(ctx):

        helpembed = discord.Embed(title="Help", description="**Astro Bot** \nA Utilities Discord Bot with reliability and simplicity\n Made By isirk#0001", color=0x7289DA)
        helpembed.add_field(name="Info", value="@Astro Mention Me for Info")
        helpembed.add_field(name="Prefix", value="`^` (Not Customizeable)", inline=False)
        helpembed.add_field(name="Bot", value="`help`\n`info`\n`ping`")
        helpembed.add_field(name="Mod", value="`kick`\n`ban`")
        helpembed.add_field(name="Utility", value="`avatar`\n`slowmode`\n`clear`")
        helpembed.set_footer(text="Astro Bot | discord.gg/7yZqHfG")

        await ctx.send(embed=helpembed)

@client.command()
async def site(ctx):
    await ctx.send('Astro Site\nhttps://asksirk.com/Astro/')

@client.command()
async def ping(ctx):
    pingembed = discord.Embed(title="", description="", color=0x7289DA)
    pingembed.add_field(name="Pong!", value=f'`{round(client.latency * 1000)}ms`')
    await ctx.send(embed=pingembed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please mention a member")
        return
    await member.kick()
    await ctx.send(f"{member.mention} has been kicked")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to kick people")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Please mention a member")
        return
    await member.ban()
    await ctx.send(f"{member.mention} has been banned")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are not allowed to ban people")

@client.command()
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@client.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Slowmode is now {seconds} seconds.")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    
client.run('')