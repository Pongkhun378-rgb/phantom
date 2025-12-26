import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

# ---------- INTENTS ----------
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# ---------- BOT READY ----------
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Bot is running {bot.user}')
    synced = await bot.tree.sync()
    print(f'Synced {len(synced)} command(s)')

# ---------- คนเข้า ----------
@bot.event
async def on_member_join(member):
    text = f"Welcome to the EGL Phantom, {member.mention}!"
    await member.send(text)

# ---------- คนออก ----------
@bot.event
async def on_member_remove(member):
    text = f"Goodbye, {member.mention}. Thank you for coming"
    await member.send(text)

# ---------- ส่งข้อความ ----------
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'who':
        await message.channel.send('Hi I am a robot   ' + message.author.name)

    elif message.content == 'phantom':
        await message.channel.send(
            'sawaddeekub  ' + message.author.name
        )

    await bot.process_commands(message)

# ---------- PREFIX COMMAND ----------
@bot.command()
async def hi(ctx):
    await ctx.send(f"Hello {ctx.author.name}")
    
@bot.command()
async def ping(ctx, arg: str):
    await ctx.send(arg)
    
# ---------- SLASH COMMAND ----------
@bot.tree.command(name="run", description="Run bot discord")
async def run(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🚀 Bot Status",
        description="🟢 **Bot online and fully operational**",
        color=discord.Color.green(),
    )
    
    embed.add_field(
        name="User",
        value=interaction.user.mention,
        inline=False
    )
    
    await interaction.response.send_message(embed=embed)
    
@bot.tree.command(name="name", description="Say hello with your name")
@app_commands.describe(name_="What is your name?")
async def name(interaction: discord.Interaction, name_: str):
    await interaction.response.send_message(f"Hello {name_}!")
    

server_on()
# ---------- RUN ----------
bot.run(os.getenv('token'))
