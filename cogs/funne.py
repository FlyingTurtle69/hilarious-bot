import discord
from discord.ext import commands
import random

class Funne(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    @commands.command(name='copypasta', help='Responds with the pasta that matches the index. If there\'s no index, the bot will choose a random pasta', aliases=['cop'])
    async def copypasta(self, ctx, pasta=None):
        if pasta == None:
            pasta=random.choice(range(0, 14))
        pastas = [
            "Pfff haha 😂 funny very 😂 funny funny 😂 😂 😂 lolololol 😂 😂 funnies 😂 😂 laugh out loud 😂 😂 so funny 😂 😂 very funny 😂 😂 laughing laughing 😂 😂 funnies funnies 😂 😂 hahahahahahaha 😂 😂 😂 😂 😂 funny time 😂 😂 ROFL ROFL 😂 LOL 😂 XD 😂 XD 😂 XD haha 😂 funny 😂 fucking funny 😂 😂 haha 😂 ha ha ha ha ha ha XD XD XD 😂 😂 lol lol lol 😂 funny funny 😂 funnies ROFL ROFL ROFL 😂 😂super funny 😂 😂 so funny 😂 😂 hahahaha 😂 XD 😂XD 😂 XD 😂XD 😂 XDDDDD 😂 😂 XXXXDDDD 😂 😂 haha 😂 ha ha 😂 haha 😂ha ha 😂 funny funny funny 😂 😂so funny 😂 so very funny 😂 😂 so fucking funny 😂 😂 😂 hahahahah 😂 😂 LOL LOL LOL 😂 XD 😂 LOL 😂 laughing out loud 😂 funny laughing 😂 ha ha ha 😂 😂 😂 😂 funnies 😂 too funny 😂 😂",
            "To yeet, or not to yeet-that is the question: Whether 'tis danker in the mind to yeet The slings and arrows of dank fortune Or to yeet arms against a sea of troubles And by yeeting end them. To yeet, to yeet- No more--and by a sleep to say we yeet The heartache, and the thousand dank shocks That fiesh yeets heir to. Tis a consummation Devoutly to yeet yeeted. To yeet, to yeet- To yeet-perchance to yeet: ay, there's the rub, For in that sieep of death what dreams may yeet When we have yeeted off this dank coil, Must yeet us pause. There yeets the respect That yeets calamity of so dank life. For who would yeet the whips and scorns of time, Th' oppressor yeets wrong, the dank man's contumely The pangs of dank love, the law's delay. The insolence of office, and the spurns That dank merit of th' dank takes, When he himself might his quietus yeet With a dank bodkin? Who would fardeisy s yeet, To yeet and yeet under a dank life. But that the dread of something after death, The dank country, from whose bourn No traveller yeets, yeets the will, And makes us rather yeet those ils we yeet Than yeet to others that we yeet not of? Thus conscience does yeet cowards of us all, And thus the dank hue of resolution Is yeeted o'er with the dank cast of thought, And enterprise of dank pitch and moment With this regard their currents yeet dank And yeet the name of action. - Soft you now, The dank Ophelia! - Nymph, in thy orisons Yeet all my sins veeted",
            "Okay let’s see what we’re working with\nWhoa\nNice chungus\nBig, but not too normie\nBreathtaking length\nA 69 (nice)° angle\nEh, could trim the hairs a bit but we’ll work on it\nYep... I’d say that’s a pretty big chungus\nI rate it... wholesome 85/100\nGood job, kind redditor",
            'The other day, I (23M) was driving my car on my way to my mother’s house (25F) on the way, I (23M) saw a Kindergarten class consisting of 17 children (5F) (6M) (6M) (6F) (5F) (5M) (6F) (5M) (5F) (6M) (5M) (6F) (5M) (6M) (6F) (5M) (6F) crossing the street. I (23M) really had to get to my mom’s house, so I (23M) couldn’t stop. See, she has a clock that is very old-timey. She called me (23M) and said “the clock says 6:09 lol epic!” And I (23M) had to get their in time to take a picture and post it to Reddit for the Karma. I (23M) tried to swerve out of the way but ended up hitting and killing all 17 of the children  (5F) (6M) (6M) (6F) (5F) (5M) (6F) (5M) (5F) (6M) (5M) (6F) (5M) (6M) (6F) (5M) (6F) am I the asshole? The cops are on their way and I need proof I’m innocent.',
            "⠀⠀⠀⢀⡤⢶⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n⠀⠀⢀⣠⣤⣤⣤⣿⣧⣀⣀⣀⣀⣀⣀⣀⣀⣤⡄⠀ \n⢠⣾⡟⠋⠁⠀⠀⣸⠇⠈⣿⣿⡟⠉⠉⠉⠙⠻⣿⡀ \n⢺⣿⡀⠀⠀⢀⡴⠋⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠙⠇ \n⠈⠛⠿⠶⠚⠋⣀⣤⣤⣤⣿⣿⣇⣀⣀⣴⡆⠀⠀⠀ \n⠀⠀⠀⠀⠠⡞⠋⠀⠀⠀⣿⣿⡏⠉⠛⠻⣿⡀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠈⠁⠀⠀ ⠀\n⠀⣠⣶⣶⣶⣶⡄⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀ ⠀\n⢰⣿⠟⠉⠙⢿⡟⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀ ⠀\n⢸⡟⠀⠀⠀⠘⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀ ⠀\n⠈⢿⡄⠀⠀⠀⠀⠀⣼⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀ ⠀\n⠀⠀⠙⠷⠶⠶⠶⠿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀",
            "Wholesome 100 😂🤣😂😂😂\n[Everyone liked that]😂😂🤣😂\nBecause that's what heroes do.😂😂😂\nHuzzah! A man of quality!😂😂\nNo, no. He's got a point😂😂😂🤣😂😂😂\nThey had us in the first half, not gonna lie 🤣🤣",
            "That's the funniest thing I've ever seen. Peak of comedy right here. I can't believe how incredibly funny this is. You have got me off my seat and rolling around the floor laughing. Your comedic talent hasn't been seen since the days of Seinfeld. Your comedic charisma is so captivating I just can't stop laughing. Your father must be so proud of you, I know I would be. You may have just created the new standard for comedy for hundreds of years to come. Historians will look back at this precise moment with astonishment, trying to comprehend how anyone could have this incredible talent at comedy. Scientists will undoubtedly create the FQ, the Funny Quotient, in respect of all your comedic achievements. But none will have as much FQ as you. Once the day comes that you will have to leave this earth, the entire world will mourn you for years. We may never know when the next comedic talent may come enlighten the world with their comedy.",
            "As an ER tech, the worst yeast infection I ever saw was in the foreskin of a man's penis, made more serious by genital warts, some brewing necrotizing fasciitis, and a catheter that hadn't been changed in several days. He only came in because he tried to hire a sex worker and no one would let him fold the catheter over his pus-filled, partially necrotic member so he could stick it in them. A friend of mine is a nurse and was with a doc doing a pelvic exam on a woman who'd complained of excessive discharge. The first thing the doc asked for was a trash can to catch the discharge because it was creating a puddle on the floor.",
            "**FAQ: I just shit and cum at your comment**\n**What does this mean?**\nThe amount of shit (and cum) on my computer and floor has increased by one.\n**Why did you do this?**\nThere are several reasons I may deem a comment to be worthy of feces or ejaculation. These include, but are not limited to:\n - Being gay\n - Dank copypasta bro, where'd you find it\n - walter\n**Am I going to shit and cum too?**\nNo - not yet. But you should refrain from shitposting and cumposting like this in the future. Otherwise I will be forced to shit and cum again, which may put your shitting and cumming privileges in jeopardy.\n**I don't believe my comment deserved being shit and cum at. Can you un-cum it?**\nSure, mistakes happen. But only in exceedingly rare circumstances will I put shit back into my butt. If you would like to issue an appeal, shoot me a hot load explaining what I got wrong. I tend to respond to retaliatory ejaculation within several minutes. Do note, however, that over 99.9% of semen dies before it can fertilize the egg, and yours is likely no exception.\n**How can I prevent this from happening in the future?**\nAccept the goopy brown and white substance and move on. But learn from this mistake: your behavior will not be tolerated in my mom's basement. I will continue to shit and cum until you improve your conduct. Remember: ejaculation is privilege, not a right.",
            "Tweedlecock and Tweedleball\nAgreed to have some torture;\nFor Tweedlecock said Tweedleball\nHad molested his daughter.\nJust then flew down a moderator,\nSo gay and so retarded;\nWho banned the Pewdiepie submitters,\nEpic wholesome one hundred.",
            "Bro, that's like... possibly one of the most interesting things I have ever heard in my entire lifespan on this wonderful habitable planet that we call earth. I am completely and utterly flabbergasted by how profound that statement of yours was. You may have just done something revolutionary; maybe even pioneered a new era of human knowledge. Unfortunately for you, though, it seems that I literally could not give less of a fuck. There exists not a powerful enough electron microscope to visualize how little I care. The universe is estimated to contain over 100 billion galaxies, and not a single molecule in that vast expanse has asked for your opinion. Fuck you, and your prehistoric descendants. If I had one goal in life, it would be to travel back in time, find the early homo-sapien that evolved into your sorry self, and feed him to the ferocious sabre-toothed tigers of the pangaean wilderness. Nobody. Fucking. Asked.",
            'Hey! Vsauce, GLaDOS here. NICE COCK! Or is it? Just what exactly is a "nice cock"? Well, nice... means... "pleasant", "agreeable", "satisfactory". "Cock" in this context implies a section of the male genitalia. So in this context, "nice cock" means a male penis that is pleasant, "agreeable", or "satisfactory", most likely in reference to... sex. Although many people use the words "sperm" and "semen" as if they were synonymous, the truth is that sperm comprises only about 5-10% of any give male jizzload. The rest is comprised of rich, bodily fluids and a dazzling array of nutrients. Yummy! Semen also has antidepressant qualities. A mood-enhancing potion that contains Estrogen, Cortisol, Oxytocin, Melatonin, and Serotonin. It\'s a wonder that people don\'t eat more of it. BUT ENOUGH ABOUT THAT! I want to know more about what makes your penis thick. So... Make sure to let me know in the comments down below. ALSO MAKE SURE TO SMASH THAT LIKE BUTTON, SUBSCRIBE, NOTIFICATION BELL AND SHARE THIS VIDEO WITH YOUR LOVED ONES if you found it insightful.',
            "when i was younger, i was plagued by wet dreams of Homer Simpson. i didn't find him attractive at all, but he would show up in my dreamscape, brutally nude, and the next thing i knew i would wake up to find that i had bedwet thick. the problem was amplified in college, where my roommate was able to smell my nocturnal emissions and got concerned at their frequency. after years of sleeping in cummy sheets and shame, i finally took action. i built a makeshift sex doll to look like Homer and had vigorous, sweaty sex with it until i cummed in his yellow ass. after that, no more Homer sex dreams",
            "Freshman year in high school, straight up Greg heffley moment. My crush at the time was looking at me, and smiling. She was wearing this push up bra and a skintight shirt (didn’t know her titties were actually smaller when I saw them a few years later.. big disappointment tbh) I made eye contact, and smiled. She giggled, and blushed, I could see it, her friends were talking about how “good looking and sweet” I was, however this would soon vanish when the sexual thoughts attacked my frontal lobe. BOOM! Out of no where, the largest log the class has ever seen started to awake like a garden snake out of hibernation. This was no garden snake however, for the reticulated python was starting to pierce through my shorts in front of the whole class. There I was, my giant Shlong making its presence known in my maroon red AFJROTC Shorts. I was embarrassed, but kept pushing on with my presentation, thinking about Jesus to try and make my boner disappear. It was too late, the whole class had born witness to my throbbing erection. My crush, who I thought would be laughing had the most shocked look on her face. My teacher, shocked that I was still up there and not running out of the class, nodded in respect as he told me to cut the presentation short, and find my seat. My boner, now dissipating, me coming to my senses and realizing how embarrassing this journey was. The class was silent, for the rest of the day, knowing how me, instead of trying to hide my erection, decided to assert its presence to the crowd. Years later, I saw my crush naked. I was too embarrassed to ask her out for years after my penis basically broke physics within my shorts in the class. I know now, why she actually liked me, hoes just want the dick man. That is my story, and I stick by it every fucking day."
        ]
        try:
            await ctx.send(pastas[int(pasta)])
        except Exception:
            await ctx.send('You must use a whole number between (inclusive) 0 and 13 as the index')
            await help(ctx, 'copypasta')

    @commands.command(name='michael', aliases=['m'], help='Sends a random pic of michael')
    async def michael(self, ctx):
        pic = random.choice(range(1, 38))
        await ctx.channel.send(file=discord.File(f'assets/michael/{pic}.jpg'))

    @commands.command(name='finley', aliases=['f'], help='Sends a pic of finley')
    async def finley(self, ctx):
        await ctx.channel.send(file=discord.File('assets/finley.jpg'))

    @commands.command(name='kai', aliases=['k'], help='Sends a wave of <:kaiscared:686868984317870100>. This won\'t work unless the server has a :kaiscared: emoji')
    async def kai(self, ctx):
        for _ in range(1, 12):
            await ctx.send('<:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100>\n<:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100>\n<:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100><:kaiscared:686868984317870100>')

    @commands.command(name='jacob', aliases=['j'], help='jk bro')
    async def jacob(self, ctx):
        await ctx.send('jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro jk bro')

    @commands.command(name='bingus', help='bingus')
    async def bingus(self, ctx):
        await ctx.channel.send(file=discord.File('assets/bingus.png'))

    tobyPhrases = [
        "Retard",
        "Hey retard",
        "You are a retard",
        "Def the retard",
        "Ytr",
        "Anyone wanna play league?",
        "Tardre",
        "Aitr? Yes.",
        "something retarded",
    ]

    @commands.command(name='toby', aliases=['t'], help='random funne')
    async def toby(self, ctx):
        phrase = random.choice(Funne.tobyPhrases)
        await ctx.send(phrase)

    @commands.command(name='spoiler', help='Sends a spoiler')
    async def spoiler(self, ctx):
        await ctx.send(file=discord.File('assets/SPOILER_spoiler.png'))

def setup(bot):
    bot.add_cog(Funne(bot))