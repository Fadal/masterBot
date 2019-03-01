from discord.ext.commands import Bot
from discord import user, server
from discord import Game
import random
import discord
import time

BOT_PREFIX = "!"
TOKEN = "NTUwNTA0NjEyNTU4NDA1NjQ0.D1jbtA.NnfssXHl678qngKbs87oBONLuOM"
client = Bot(command_prefix=BOT_PREFIX)

@client.command(description = "Calculate an age of a given year", pass_context = True)
async def age(ctx, message):
    year = 0
    try:
        year = int(message)

    except ValueError:
        await client.say("Not a valid input, please enter a valid number")

    current_year = 2019
    calculated_age = current_year - year
    await client.say("If born in " + message + " you should be " + str(calculated_age) + " years old")

@client.command(description = "Will roast the hell out of any nigga for you")
async def roast(roastee: discord.User):
    list_of_roasts = ["If laughter is the best medicine, your face must be curing the world.",
    "You're so ugly, you scared the crap out of the toilet.",
    "Your family tree must be a cactus because everybody on it is a prick.",
    "No I'm not insulting you, I'm describing you.",
    "It's better to let someone think you are an Idiot than to open your mouth and prove it.",
    "If I had a face like yours, I'd sue my parents.",
    "Your birth certificate is an apology letter from the condom factory.",
    "I guess you prove that even god makes mistakes sometimes.",
    "The only way you'll ever get laid is if you crawl up a chicken's ass and wait.",
    "You're so fake, Barbie is jealous.",
    "I’m jealous of people that don’t know you!",
    "My psychiatrist told me I was crazy and I said I want a second opinion. He said okay, you're ugly too.",
    "You're so ugly, when your mom dropped you off at school she got a fine for littering.",
    "If I wanted to kill myself I'd climb your ego and jump to your IQ.",
    "You must have been born on a highway because that's where most accidents happen.",
    "Brains aren't everything. In your case they're nothing."
    "I don't know what makes you so stupid, but it really works.",
    "I can explain it to you, but I can’t understand it for you.",
    "Roses are red violets are blue, God made me pretty, what happened to you?",
    "Behind every fat woman there is a beautiful woman. No seriously, your in the way.",
    "Calling you an idiot would be an insult to all the stupid people.",
    "You, sir, are an oxygen thief!",
    "Some babies were dropped on their heads but you were clearly thrown at a wall.",
    "Don't like my sarcasm, well I don't like your stupid.",
    "Why don't you go play in traffic.",
    "Please shut your mouth when you’re talking to me.",
    "I'd slap you, but that would be animal abuse.",
    "They say opposites attract. I hope you meet someone who is good-looking, intelligent, and cultured.",
    "Stop trying to be a smart ass, you're just an ass.",
    "The last time I saw something like you, I flushed it."]

    random.seed(time.time())
    fire_roast = random.choice(list_of_roasts)
    await client.say(roastee.mention + ", " + fire_roast)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)