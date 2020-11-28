import discord
from discord.ext import commands
from discord.utils import get

class Voice(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(name='microwave', help="Joins the voice channel you're in and plays a microwave noise")
    async def microwave(self, ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        voice.play(discord.FFmpegPCMAudio(executable="C:/Program Files (x86)/FFmpeg for Audacity/ffmpeg.exe", source='assets/microwave.mp3'))
        await ctx.send(f'Joined {channel}')

    @commands.command(name='SCOTLAND!!!', help="Joins the voice channel you're in and plays scotland forever")
    async def SCOTLAND(self, ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        voice.play(discord.FFmpegPCMAudio(executable="C:/Program Files (x86)/FFmpeg for Audacity/ffmpeg.exe", source='assets/scotland.mp3'))
        await ctx.send(f'Joined {channel}')

    @commands.command(name='leave', help="Leaves the voice channel the bot is currently in")
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        await server.disconnect()
        await ctx.send(f'Left {channel}')

def setup(bot):
    bot.add_cog(Voice(bot))