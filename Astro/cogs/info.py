from multiprocessing.connection import Client
import discord
from discord import Embed
from discord.ext import commands
from discord.shard import ShardInfo
from discord.user import User
from discord.utils import get
from datetime import datetime
import os
import collections
import time, datetime

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        '''Get information about the bot.'''
        infoembed = discord.Embed(title="Info", description="A Utilities Discord Bot with reliability and simplicity", color=0x7289DA)
        infoembed.set_author(name=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        infoembed.add_field(name= "<:news:758781954073821194> News", value="<:translate:758449663517917195> Translators Needed. <:translate:758449663517917195>\nIf you can speak another language fluently or know someone who can DM isirk#0001.", inline=True)
        infoembed.set_thumbnail(url="https://cdn.discordapp.com/emojis/758451109919981580.png?v=1")
        infoembed.add_field(name= ":link: Links", value="[Bot Site](https://asksirk.com/Astro) \n[Github Repository](https://github.com/ISIRK/Astro) \n[Patreon](https://www.patreon.com/Astro_Bot)", inline=False)
        infoembed.add_field(name="About", value="Version 1.0 **Public Beta**\nMade with :heart: in <:python:758139554670313493>\nOwned, Developed, and Run by isirk#0001", inline=False)
        infoembed.set_footer(text="Astro Bot | discord.gg/7yZqHfG")
        await ctx.send(embed=infoembed)

    @commands.command()
    async def help1(self, ctx):
        '''Old/New help command that is being worked on right now.'''
        helpembed = discord.Embed(title="Help", description="A Utilities Discord Bot with reliability and simplicity\n Made By isirk#0001", color=0x7289DA)
        helpembed.set_author(name=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        helpembed.add_field(name="Prefix", value="`^` (Not Customizeable)", inline=False)
        helpembed.add_field(name="Bot", value="`help`\n`info`\n`ping`\n`support`")
        helpembed.add_field(name="Mod", value="`kick`\n`ban`\n`mute`\n`unmute`")
        helpembed.add_field(name="Utility", value="`avatar`\n`slowmode`\n`clear`\n`server`\n`user`")
        helpembed.set_footer(text="Astro Bot | discord.gg/7yZqHfG")

        await ctx.send(embed=helpembed)

    @commands.command()
    async def support(self, ctx):
        '''Get support information.'''
        supportembed = discord.Embed(title="Support", color=0x7289DA)
        supportembed.set_author(name=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        supportembed.set_thumbnail(url="https://cdn.discordapp.com/emojis/758453150897799172.png?v=1")
        supportembed.add_field(name="Support Server", value="Support Server: https://discord.gg/7yZqHfG", inline=False)
        supportembed.add_field(name="Contact", value="To contact dm isirk#0001 or email me @ isirk@asksirk.com", inline=False)
        supportembed.add_field(name=":link: Links", value="Bot Site: https://asksirk.com/Astro\nGithub Repository: https://github.com/ISIRK/Astro\nPatreon: https://www.patreon.com/Astro_Bot", inline=False)
        supportembed.set_footer(text="Use [prefix] help or info.")
        await ctx.send(embed=supportembed)
    
    @commands.command()
    async def invite(self , ctx):
        '''Get the invite for the bot.'''
        embed = discord.Embed(title="Invite", color=0x7289DA)
        embed.add_field(name="Contact", value="Unfortunately Astro Bot is a Private Bot.\nIf You want to invite Astro into your server\n**DM isirk#0001 on discord with the format below:**\n```\nName:(Discord Tag)\nServer Name:\nServer Invite:\nAmmount of Members:\nWhy you want Astro in your server:\n(Optional)Any other thing you want me to know?\n```", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/758138226874908705/758729610237837372/astro.png")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def about(self, ctx):
        """Tells you information about the bot itself."""

        revision = self.get_last_commits()
        embed = discord.Embed(description='Latest Changes:\n' + revision)
        embed.title = 'Official Bot Server Invite'
        embed.url = 'https://discord.gg/DWEaqMy'
        embed.colour = discord.Colour.blurple()

        owner = self.bot.get_user(self.bot.owner_id)
        embed.set_author(name=str(owner), icon_url=owner.avatar_url)

        # statistics
        total_members = 0
        total_unique = len(self.bot.users)

        text = 0
        voice = 0
        guilds = 0
        for guild in self.bot.guilds:
            guilds += 1
            total_members += guild.member_count
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    text += 1
                elif isinstance(channel, discord.VoiceChannel):
                    voice += 1

        embed.add_field(name='Members', value=f'{total_members} total\n{total_unique} unique')
        embed.add_field(name='Channels', value=f'{text + voice} total\n{text} text\n{voice} voice')

        memory_usage = self.process.memory_full_info().uss / 1024**2
        cpu_usage = self.process.cpu_percent() / psutil.cpu_count()
        embed.add_field(name='Process', value=f'{memory_usage:.2f} MiB\n{cpu_usage:.2f}% CPU')

        version = pkg_resources.get_distribution('discord.py').version
        embed.add_field(name='Guilds', value=guilds)
        embed.add_field(name='Commands Run', value=sum(self.bot.command_stats.values()))
        embed.add_field(name='Uptime', value=self.get_bot_uptime(brief=True))
        embed.set_footer(text=f'Made with discord.py v{version}', icon_url='http://i.imgur.com/5BFecvA.png')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))