import discord
from discord.ext import commands

import random
import emoji
import asyncio
from datetime import datetime, timedelta

class Utility(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    otherEmojis = {
        '1': ':one:',
        '2': ':two:',
        '3': ':three:',
        '4': ':four:',
        '5': ':five:',
        '6': ':six:', 
        '7': ':seven:',
        '8': ':eight:',
        '9': ':nine:',
        '0': ':zero:',
        '!': ':exclamation:',
        '?': ':question:',
        '#': ':hash:',
        '*': ':asterisk:',
    }

    reactEmojis = {
        'a': '🇦',
        'b': '🇧',
        'c': '🇨',
        'd': '🇩',
        'e': '🇪',
        'f': '🇫',
        'g': '🇬',
        'h': '🇭',
        'i': '🇮',
        'j': '🇯',
        'k': '🇰',
        'l': '🇱',
        'm': '🇲',
        'n': '🇳',
        'o': '🇴',
        'p': '🇵',
        'q': '🇶',
        'r': '🇷',
        's': '🇸',
        't': '🇹',
        'u': '🇺',
        'v': '🇻',
        'w': '🇼',
        'x': '🇽',
        'y': '🇾',
        'z': '🇿',
    }

    alternativeEmojis = {
        'a': '🅰️',
        'b': '🅱️',
        'o': '🅾️',
        'i': 'ℹ️'
    }

    def addToString(letter, tempEmojifiedPhrase):
        if letter.isalpha():
            tempEmojifiedPhrase += f':regional_indicator_{letter}:'
        elif letter in Utility.otherEmojis:
            tempEmojifiedPhrase += Utility.otherEmojis[letter]
        else:
            tempEmojifiedPhrase += letter
        return tempEmojifiedPhrase

    @commands.command(name='emojify', help='Turns text into emojis. To get the message-ID, hold shift over the message you want then click Copy ID. Then delete everything before and including the hyphen', aliases=['e', 'emoji', '🇪'])
    async def emojify(self, ctx, phrase, messageId=None):
        if messageId == None: 
            emojifiedPhrase = ''
            tempEmojifiedPhrase = ''

            for letter in phrase.lower():
                tempEmojifiedPhrase = Utility.addToString(letter, tempEmojifiedPhrase)
                
                if len(tempEmojifiedPhrase) > 2000:
                    await ctx.send(emojifiedPhrase)
                    tempEmojifiedPhrase = ''
                    tempEmojifiedPhrase = Utility.addToString(letter, tempEmojifiedPhrase)
                else:
                    emojifiedPhrase = tempEmojifiedPhrase
            await ctx.send(emojifiedPhrase)
        else:
            message = await ctx.fetch_message(int(messageId))
            i = 0
            alreadyUsed = {}
            for letter in phrase.lower():
                if letter in Utility.reactEmojis:
                    if alreadyUsed.get(letter, False) != True:
                        await message.add_reaction(Utility.reactEmojis[letter])
                        i += 1
                        alreadyUsed[letter] = True
                    else:
                        await message.add_reaction(Utility.alternativeEmojis.get(letter, Utility.reactEmojis[letter]))
                        i += 1
                elif letter in emoji.UNICODE_EMOJI:
                    await message.add_reaction(letter)
                    i += 1
                if i == 20:
                    break

    @commands.command(name='roll', help='Simulates rolling dice. You can\'t use more than 500 dice and have more than 1000 sides')
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        if number_of_dice > 500:
            await ctx.send('That\'s too many dice')
            return
        if number_of_sides > 1000:
            await ctx.send("That's too many sides")
            return
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(','.join(dice))

    @commands.command(name='poll',help='Creates a yes/no poll. The duration is in minutes.')
    async def poll(self, ctx, question, duration=60.0):
        embed = discord.Embed(title=question, colour=discord.Color.red(), description="React with ✅ for yes. React with ❎ for no.", timestamp=datetime.utcnow() + timedelta(minutes=duration))
        embed.set_author(name=f"{ctx.message.author.display_name}'s Poll", icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text='Ends ')
        bot_message = await ctx.send(embed=embed)
        await bot_message.add_reaction('✅')
        await bot_message.add_reaction('❎')
        await asyncio.sleep(float(duration) * 60)
        updated_msg = await ctx.fetch_message(bot_message.id)
        embed = discord.Embed(title=question, colour=discord.Color.red(), timestamp=datetime.utcnow())
        embed.set_author(name=f"{ctx.message.author.display_name}'s Poll", icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text='Ended')
        embed.add_field(name='Results', value=f'{updated_msg.reactions[0].emoji} {updated_msg.reactions[0].count - 1}　 {updated_msg.reactions[1].emoji} {updated_msg.reactions[1].count - 1}')
        await bot_message.edit(embed=embed)
        await bot_message.clear_reactions()

    @commands.command(name='report', help=f'Sends your message to the dev')
    async def report(self, ctx, *, message):
        me = self.bot.get_user(345767813664866304)
        await me.send(f'<@!{ctx.author.id}> reported the following: ```{message}```')
        await ctx.send('Message reported')

def setup(bot):
    bot.add_cog(Utility(bot))