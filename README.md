# Hilarious Bot
 Discord bot that does many different things. Created for my friend's server. Default prefix is `&`.
 Invite the bot to your server [here](https://discord.com/api/oauth2/authorize?client_id=724141587369689088&permissions=3533888&scope=bot)

## &copypasta
The following keywords can be used to make the bot send the specific copypasta:
- [funny](https://www.reddit.com/r/copypasta/comments/hdfkq8/funy/)
- [yeet](https://www.reddit.com/r/copypasta/comments/geuex1/to_yeet_or_not_to_yeet/)
- [chungus](https://www.reddit.com/r/copypasta/comments/ghezgt/kronk_rates_your_chungus/)
- [aita](https://www.reddit.com/r/copypasta/comments/hjfei3/aita_for_murdering_17_children/)
- [f](https://www.reddit.com/r/copypasta/comments/h8v92y/f/)
- [wholesome](https://www.reddit.com/r/okbuddyretard/comments/gh3nqx/trust_me_it_makes_it_funnier/fq73jx6/?context=3)
- [funniest](https://www.reddit.com/r/copypasta/comments/gak2kc/funniest_thing_ive_ever_seen_wrote_this_myself_in/)
- [er](https://www.reddit.com/r/MakeMeSuffer/comments/g9cjo8/absolute_suffering/fosrznt/?context=3)
- [faq](https://www.reddit.com/r/copypasta/comments/fwkfyq/faq_i_just_shit_and_cum_at_your_comment/)
- [tweedlecock](https://www.reddit.com/r/okbuddyretard/comments/fgu6o7/subscriptions_by_day/fk6x510/?context=3)
- [nobody](https://www.reddit.com/r/copypasta/comments/etlw8e/nobody_fucking_asked/)
- [glados](https://www.reddit.com/r/copypasta/comments/g2aqnl/hey_vsauce_glados_here_nice_cock/)
- [homer](https://www.reddit.com/r/copypasta/comments/e1bx2s/wet_dreams_of_homer_simpson_credit_to_ucummy_boner/)
- [greg](https://www.reddit.com/r/copypasta/comments/c3zskd/credit_to_ufuckthestate1776_in_the_comments_of_an/)
- [guy](https://www.reddit.com/r/195/comments/ilsbi8/the_guy/g3uiry6/?context=3)
- [hentai](https://www.reddit.com/r/copypasta/comments/ilx5fb/bitches_in_hentai_be_like/)
- [twump](https://www.reddit.com/r/copypasta/comments/i9e6zf/trump_has_a_massive_cock/g1eiby1/?context=3)
- [gaming](https://www.reddit.com/r/dogelore/comments/iuvny6/another_gamer_oppressed_by_society/g5o3ny0/?context=3)

## Permissions Explained
These are the required permissions and the reasoning behind them. If you aren't going to use all features of the bot, feel free to not grant permissions which are unnecessary.
- **Read Messages** and **Send Messages**: So the bot can see and send anything
- **Manage Messages**: The bot removes the counted emoji when someone reacts with it to their own message. For example, the server has 😎 as the counted emoji and someone messages hi and reacts to their own message with 😎. The bot then deletes that reaction. Also, this permission is needed so when a poll ends, it can remove the reactions
- **Embed Links**: Many commands use embeds instead of normal text because it looks nicer, for example &profile
- **Attach Files**: Needed to send pictures for commands like &michael
- **Read Message History**: &emojify reactions and finalising the results for &poll
- **Add Reactions**: The bot adds the check mark and cross emojis when someone makes a poll
- **Use External Emojis**: &kai
- **Connect** and **Speak**: Voice commands like &microwave

## Self-Hosting
If you want to host the bot on your own, you will need to follow this. 

### Requirements
- Python 3 (I'm not sure exactly which version but I use 3.8.3)
- [discord.py[voice]](https://discordpy.readthedocs.io/en/latest/intro.html#installing)
- [emoji](https://pypi.org/project/emoji/)

### Setup
1. Go to https://discord.com/developers/applications and login
2. Click `New Application` in the top right hand corner, call it whatever you want then click `Create`
3. Click `OAuth2` (on the left) and in `SCOPES` click `bot`
4. Scroll down and in `BOT PERMISSIONS` select the following:
    - View Channels
    - Send Messages
    - Manage Messages
    - Embed Links
    - Attach Files
    - Read Message History
    - Add Reactions
    - Connect
    - Speak
5. Go to the link generated in `SCOPES`
6. Add the bot to your server
7. Go back to the other page and click `Bot` then `Add Bot` and `Yes, do it!`
8. Under `TOKEN` click `Copy`
9. Download the [ZIP](https://github.com/FlyingTurtle69/hilarious-bot/archive/main.zip) for this code and extract it
10. Run `setup.py`
11. Paste the token you copied before and click enter

Now whenever you want to run the bot just run `bot.py` and keep the window open until you want to stop it

## To Do
- Make &help command not one massive list. Either:
    - Make it paginate or
    - Make it link to a wiki page