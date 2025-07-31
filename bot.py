import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def join(ctx):
    """Join the author's voice channel."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not connected to a voice channel.")

@bot.command()
async def play(ctx, url: str):
    """Play audio from a URL in the voice channel."""
    voice_client = ctx.voice_client
    if not voice_client:
        if ctx.author.voice:
            voice_client = await ctx.author.voice.channel.connect()
        else:
            await ctx.send("Join a voice channel first.")
            return

    source = discord.FFmpegPCMAudio(url)
    if voice_client.is_playing():
        voice_client.stop()
    voice_client.play(source)
    await ctx.send(f"Now playing: {url}")

@bot.command()
async def leave(ctx):
    """Disconnect from the voice channel."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not connected to a voice channel.")

bot.run(TOKEN)
