# import os
import random
import json
import asyncio
from datetime import datetime

import sqlite3
from contextlib import closing
import re

import discord
from discord.ext import commands, tasks
from discord.utils import get

with open("token.0", "r", encoding="utf-8") as tf:
    TOKEN = tf.read()

def read_server(column, serverID):
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            try:
                return cursor.execute(f"SELECT {column} FROM servers WHERE serverID = ?", (serverID,)).fetchone()[0]
            except:
                return None

def write_server(column, newValue, serverID):
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(f"INSERT OR REPLACE INTO servers (serverID, {column}) VALUES (?, ?)", (serverID, newValue))
        connection.commit()


def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or("&")(bot, message)

    prefix = read_server('prefix', message.guild.id)
    if prefix == None:
        return commands.when_mentioned_or("&")(bot, message)
    
    return commands.when_mentioned_or(prefix)(bot, message)

def get_reaction(message):
    if not message.guild:
        return '😎'
    
    reaction = read_server('reaction', message.guild.id)
    if reaction == None:
        return '😎'
    
    return reaction
    
bot = commands.Bot(command_prefix=get_prefix)

initial_extensions = ['cogs.voice', 'cogs.funne', 'cogs.utility']
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.remove_command('help')

commandUsage = {
    'prefix': '<prefix>',
    'copypasta': '[pasta-index]',
    'roll': '<number-of-dice> <number-of-sides>',
    'based': '<user>',
    'cringe': '<user>',
    'profile': '[user]',
    'leaderboard': '<type>',
    'gamble': '<amount> <side>',
    'poll': '"<question>" [duration]',
    'report': '<message>',
    'help': '<command>',
    'reaction': '<emoji>',
    'emojify': '"<phrase>" [message-ID]',
}
commandExamples = {
    'prefix': '```{0}prefix $``````{0}prefix so theres this guy and```',
    'copypasta': '```{0}copypasta``````{0}cop 4```',
    'roll': '```{0}roll 69 2``````{0}roll 2 6```',
    'based': '```{0}based @Hilarious Bot``````{0}b @℉ℓℽℹℕℊ ╤¥ℝτ⅊ℇ```',
    'cringe': '```{0}cringe @Hilarious Bot``````{0}c @℉ℓℽℹℕℊ ╤¥ℝτ⅊ℇ```',
    'profile': '```{0}profile``````{0}p @Hilarious Bot```',
    'leaderboard': '```{0}leaderboard based``````{0}l cringe``````{0}top 😎```',
    'gamble': '```{0}gamble 1 heads``````{0}gamble 5 t```',
    'poll': '```{0}poll "Is this bot epic?"``````{0}poll "Have I wasted a lot of time on this?" 120```',
    'report': "```{0}report It's broken lol```",
    'reaction':"```{0}reaction 😂``````{0}reaction 🤔```",
    'emojify': '```{0}emojify "bruh moment"``````{0}e "hm🤔 baba" 781786505298968576```'
}

async def is_guild_admin(ctx):
    return ctx.author.guild_permissions.administrator

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord at {datetime.now().strftime("%I:%M%p %d %B")}\n')
    await bot.change_presence(activity=discord.Game(name='ur mum'))
    hourlyLoop.start()


def justNumbers(text):
    return int(re.sub('\D', '', text))

async def changeScore(scoreType, userID, change, context=None):
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            try:
                currentScore = int(cursor.execute(f"SELECT {scoreType} FROM scores WHERE userID = ?", (userID,)).fetchone()[0])
            except:
                cursor.execute(f"INSERT INTO scores (userID, {scoreType}) VALUES (?, 1)", (userID,))
                currentScore = 1
            else:
                currentScore += change
                cursor.execute(f"UPDATE scores SET {scoreType} = ? WHERE userID = ?", (currentScore, userID))   
            if context != None:
                await context.send(f"<@{userID}> is {scoreType}\nTheir {scoreType} score is now {currentScore}")
        connection.commit()

@bot.event
async def on_reaction_add(reaction, user):
    reactions = get_reaction(reaction.message)
    if str(reaction.emoji) == reactions:
        if reaction.message.author != user:
            await changeScore('pog', reaction.message.author.id, 1)
        else:
            dm = await user.create_dm()
            await dm.send(f"<@!{user.id}>, you can't pog at your own message")
            await reaction.message.remove_reaction(reaction.emoji, user)

@bot.event
async def on_raw_reaction_remove(RawReactionActionEvent):
    # idk what happened but i had to change this to on_raw cause it wasn't being called for no apparant reason
    message = await bot.get_channel(RawReactionActionEvent.channel_id).fetch_message(RawReactionActionEvent.message_id)
    reactions = get_reaction(message)
    if str(RawReactionActionEvent.emoji) == reactions:
        if message.author.id != RawReactionActionEvent.user_id:
            await changeScore('pog', message.author.id, -1)

@bot.command(name='based', help="Increases the specified user's based score", aliases=['b'])
async def based(ctx, user):
    userID = justNumbers(user)
    #Checks if the user who called the command is calling themselves based and checks that they input a user
    if userID == ctx.author.id:
        await ctx.send("You can't call yourself based, retard")
        return
    if user[0] != '<' or user[1] != '@':
        await ctx.send("You have to write a user, retard")
        return

    await changeScore('based', userID, 1, ctx)

@bot.command(name='cringe', help="Increases the specified user's cringe score", aliases=['c'])
async def cringe(ctx, user):
    userID = justNumbers(user)
    #Checks if the user who called the command is calling themselves cringe and checks that they input a user
    if userID == ctx.author.id:
        await ctx.send("You can't call yourself cringe, retard")
        return
    if user[0] != '<' or user[1] != '@':
        await ctx.send("You have to write a user, retard")
        return
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            try:
                shieldTimeLeft = int(cursor.execute("SELECT shieldTimeLeft FROM scores WHERE userID = ?", (userID,)).fetchone()[0])
            except:
                shieldTimeLeft = 0        
    if shieldTimeLeft > 0:
        await ctx.send(f'{user} used a cringe shield and was protected!')
        return

    #Gives an opportunity for the victim to reverse it
    await ctx.send(f'{user}, you have 10 seconds to reply with `&reverse` to make <@!{ctx.author.id}> cringe instead.')
    global didReverse
    didReverse = [False, user, True]
    for _ in range(1,11):
        await asyncio.sleep(1)
        if didReverse[0] == True:
            break
    if didReverse[0] == True:
        user = f'<@!{ctx.author.id}>'
    else:
        await ctx.send(f'{user} was too slow!') 

    await changeScore('cringe', userID, 1, ctx)

@bot.command(name='reverse', help='Reverses when someone calls you cringe and makes them cringe instead', aliases=['uno'])
async def reverse(ctx):
    global didReverse
    if didReverse[1] == f'<@!{ctx.author.id}>' and didReverse[2] == True:
        didReverse[0] = True
        await ctx.send(f'<@!{ctx.author.id}> reversed the cringe!')
        didReverse[2] = False
    else:
        await help(ctx, 'reverse')

@bot.command(name='profile', aliases=['p','prof'], help="Shows the specified user's stats. If there's no user specified, it will show yours")
async def profile(ctx, user=None):
    reaction = get_reaction(ctx.message)
    if user is None:
        userID = ctx.message.author.id
    else:
        userID = justNumbers(user)
    username = bot.get_user(userID)
    embed = discord.Embed(colour=discord.Color.blue())
    embed.set_author(name=f"{username.name}'s Profile", icon_url=username.avatar_url)
    
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            scores = cursor.execute("SELECT * FROM scores WHERE userID = ?", (userID,)).fetchone()
            if scores == None:
                scores = (0, 0, 0, 0, 0)
    
    embed.add_field(name="Based Score", value=scores[1])
    embed.add_field(name="Cringe Score", value=scores[2])
    embed.add_field(name=f"{reaction} Count", value=scores[3])
    embed.add_field(name="Cringe Shield Time Left", value=f'{scores[4]} Hours')
    await ctx.send(embed=embed)

@bot.command(name='leaderboard', help='Shows the people with the highest scores of the specified type', aliases=['l', 'top'])
async def leaderboard(ctx, scoreType):
    based = ['based','b']
    cringe = ['cringe','c']
    reaction = ['pog', get_reaction(ctx.message)]
    if scoreType.lower() in based or scoreType.lower() in cringe or scoreType.lower() in reaction:
        if scoreType.lower() in based:
            scoreType = 'based'
        elif scoreType.lower() in cringe:
            scoreType = 'cringe'
        else:
            scoreType = 'pog'
        with closing(sqlite3.connect("data.db")) as connection:
            with closing(connection.cursor()) as cursor:
                scores = cursor.execute(f"SELECT userID, {scoreType} FROM scores ORDER BY {scoreType} DESC").fetchmany(3)

        j = 0
        description = ''
        for user in scores:
            j += 1
            description += f'**{j}. <@{user[0]}>:** {user[1]}\n'
        if scoreType == 'pog':
            scoreType = reaction[1]
        embed = discord.Embed(title=f"{scoreType.capitalize()} Leaderboard", colour=discord.Color.gold(), description=description)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'Please type either `based`, `cringe` or {reaction} as the type.')

@bot.command(name='buy', help='Buy 24 more hours of cringe shield time for 20 {0}. Note: cringe shields do not protect you from being reversed. The time is updated once every hour the bot is online.')
async def buy(ctx):
    reaction = get_reaction(ctx.message)
    userID = ctx.message.author.id
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            try:
                pogScore = int(cursor.execute("SELECT pog FROM scores WHERE userID = ?", (userID,)).fetchone()[0])
            except:
                pogScore = 0

    if pogScore > 19:
        await ctx.send(f"Are you sure you want to buy 24 more hours of cringe shield time for 20 {reaction}? `yes`/`cancel`")
    
        def check(message):
            if message.author == ctx.message.author and message.content.lower() == 'cancel':
                raise ValueError
            return message.author == ctx.message.author and message.content.lower() == 'yes'

        try:
            await bot.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Timed out')
        except ValueError:
            await ctx.send('Purchase cancelled')
        else:
            await ctx.send(f'20 {reaction} deducted and 24 hours of cringe shield time added')
            await changeScore('pog', ctx.message.author.id, -20)
            await changeScore('shieldTimeLeft', ctx.message.author.id, 24)
    else:
        await ctx.send(f'You don\'t have enough {reaction[1]}')

#This is used so that it doesnt deduct time on startup
startup = True

@tasks.loop(hours=1.0)
async def hourlyLoop():
    global startup
    if startup:
        startup = False
        return
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            shieldTimeLefts = cursor.execute("SELECT userID, shieldTimeLeft FROM scores").fetchall()

    for user in shieldTimeLefts:
        if user[1] > 0:
            await changeScore('shieldTimeLeft', user[0], -1)

@bot.command(name='gamble', help='Flips a coin. If the side you chose is flipped, the {0} you betted are doubled. If not, they are lost.')
async def gamble(ctx, amount: int, side):
    reaction = get_reaction(ctx.message)
    heads = ['h', 'head', 'heads']
    tails = ['t', 'tail', 'tails']
    if side.lower() not in heads and side.lower() not in tails:
        await ctx.send('Choose either heads or tails')
        return
    if amount < 1:
        await ctx.send(f'You must bet at least one {reaction}')
        return
    userID = ctx.message.author.id
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            try:
                pogs = int(cursor.execute("SELECT pog FROM scores WHERE userID = ?", (userID,)).fetchone()[0])
            except:
                pogs = 0

    if pogs < amount:
        await ctx.send(f'You don\'t have enough {reaction}')
        return
    flip = random.randint(0, 1)
    if flip == 0:
        result = heads
    else:
        result = tails

    if side.lower() in result:
        await ctx.send(f'You won {amount} {reaction}!')
        await changeScore('pog', ctx.message.author.id, amount)
    else:
        await ctx.send(f'You lost {amount} {reaction}')
        await changeScore('pog', ctx.message.author.id, -amount)


@bot.command(name='prefix',help='Changes the prefix of the bot for the server. You must be an admin to use this command')
@commands.check(is_guild_admin)
async def prefix(ctx, *, prefix):
    write_server('prefix', prefix, ctx.guild.id)
    await ctx.send(f'The new prefix is `{prefix}`')

@bot.command(name='reaction', help='Changes the emoji that\'s counted for the server. The default is :sunglasses:. You must be an admin to use this command')
@commands.check(is_guild_admin)
async def reaction(ctx, emoji):
    write_server('reaction', emoji, ctx.guild.id)
    await ctx.send(f'The new reaction is {emoji}')

@bot.command(name='help', help='Shows this')
async def help(ctx, command=None):
    prefix = get_prefix(bot, ctx.message)[-1]
    reaction = get_reaction(ctx.message)
    if command==None:
        embed = discord.Embed(color=discord.Color.blurple(), title='Help', description=f'To find out more about a command do: {prefix}help <command>')
        for command in bot.walk_commands():
            embed.add_field(name=f"{prefix}{command.name} {commandUsage.get(command.name, '')}", value=command.help.format(reaction), inline=False)
    else:
        found = False
        for currentCommand in bot.walk_commands():
            if currentCommand.name == command or command in currentCommand.aliases:
                found = True
                command = currentCommand
                break
        if found == False:
            await ctx.send('Command not found')
            return
        embed = discord.Embed(color=discord.Color.blurple(), title=f'Help: {command.name}')
        embed.add_field(name=f"{prefix}{command.name} {commandUsage.get(command.name, '')}", value=command.help.format(reaction), inline=False)
        aliases = []
        if not command.aliases == []:
            for aliase in command.aliases:
                aliases.append(f'`{aliase}`')
            embed.add_field(name='Aliases', value=', '.join(aliases))
        if commandExamples.get(command.name, '') != '':
            embed.add_field(name='Examples', value=commandExamples[command.name].format(prefix))
        if command.name == 'copypasta':
            embed.add_field(name='Pasta-Indicies', value="[0](https://shorturl.at/sFJR7), [1](https://shorturl.at/lnoxL), [2](https://shorturl.at/npQZ7), [3](https://shorturl.at/pFJKV), [4](https://www.reddit.com/r/copypasta/comments/h8v92y/f/), [5](https://shorturl.at/kmvBW), [6](https://www.reddit.com/r/copypasta/comments/gak2kc/funniest_thing_ive_ever_seen_wrote_this_myself_in/), [7](https://www.reddit.com/r/MakeMeSuffer/comments/g9cjo8/absolute_suffering/fosrznt/?context=3), [8](https://www.reddit.com/r/copypasta/comments/fwkfyq/faq_i_just_shit_and_cum_at_your_comment/), [9](https://www.reddit.com/r/okbuddyretard/comments/fgu6o7/subscriptions_by_day/fk6x510/?context=3), [10](https://www.reddit.com/r/copypasta/comments/etlw8e/nobody_fucking_asked/), [11](https://www.reddit.com/r/copypasta/comments/g2aqnl/hey_vsauce_glados_here_nice_cock/), [12](https://www.reddit.com/r/copypasta/comments/e1bx2s/wet_dreams_of_homer_simpson_credit_to_ucummy_boner/), [13](https://www.reddit.com/r/copypasta/comments/c3zskd/credit_to_ufuckthestate1776_in_the_comments_of_an/)")
    embed.set_footer(text='Parameters in <> are required whereas ones in [] are optional.')
    await ctx.send(embed=embed)

@bot.command(name='info', help=f'Information about the bot', aliases=['i', 'information'])
async def info(ctx):
    reaction = get_reaction(ctx.message)
    embed = discord.Embed(title='Info', colour=discord.Color.green(), description=f"This bot was made by <@!345767813664866304>\nIf you want to let me know about anything (like a suggestion or error), use the report command. Also if you want to give me money, I accept crypto. DM <@!345767813664866304> or use the report command.\n\nYou get {reaction} by people reacting to your message with the emoji")
    await ctx.send(embed=embed)

@bot.command(name='backup', help='Ignore this; only I can use it')
@commands.has_role("Personal FBI agent")
async def backup(ctx):
    await ctx.send(file=discord.File('data.db'))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct permissions for this command.')
    if Exception(error, commands.UserInputError):
        await ctx.send(f'Error: `{error}`')
        await help(ctx, ctx.command.name)


bot.run(TOKEN)