from discord.ext import commands, tasks
import discord
import os
from dotenv import load_dotenv
import apis.pont_chaban as pont_chaban
import datetime
import apis.fakeid as fakeidy
import apis.insulte as insulta
import cloudscraper
import apis.nasa as nasapi
import apis.earth as earthapi
import apis.russianRoulette as rouletteapi

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Accéder à l'ID du canal depuis les variables d'environnement
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

requests = cloudscraper.create_scraper()

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())

requests = cloudscraper.create_scraper()

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.tree.command(
    name="pont",
    description="Une commande pour se tenir au courant du lever de pont (et éviter les retards d'Alexis et Mathis)"
)
async def pont(ctx):
    embed = pont_chaban.SendPont()
    await ctx.response.send_message(embed=embed, mention_author=True)


@bot.tree.command(
    name="aide",
    description="Pour connaitre toutes les commandes à utiliser"
)
async def aide(ctx):
    embed = discord.Embed(title="Github du bot",
                      url="https://github.com/Oneloutre/le-ptit-bordelais",
                      description="__Liste des commandes :__"
                                  "\n\n 🌉 |   `/pont` : affiche les prochaines levées du pont"
                                  "\n 👤 |   `/fakeid` : Génère une fausse identité"
                                  "\n 🤬 |   `/insulte` : Génère une insulte plus ou moins polie"
                                  "\n 🗣️ |   `/addinsulte [insulte]` : Ajoute une insulte à la liste"
                                  "\n 🚀 |   `/nasa` : Envoie une image aléatoire de la NASA"
                                  "\n 🌍 |   `/earth` : Envoie une image aléatoire de la Terre"
                                  "\n 🔫 |   `/roulette` : Lance une partie de roulette russe.... attention, si vous perdez, vous êtes kick !"
                                  "\n**--------------------------------**"
                                  "\n\n ℹ️ |   `/aide` : Affiche ce menu",
                      colour=0xf500ed,
                      timestamp=datetime.datetime.now())
    embed.set_author(name="Liste des commandes disponibles")
    embed.set_thumbnail(url="https://cdn.onelots.fr/u/4ZW8nv.jpg")
    embed.set_image(url="https://cdn.onelots.fr/u/HiJNgf.png")
    embed.set_footer(text="With ❤️ by Mathis & Roch", icon_url="https://cdn.onelots.fr/u/EQndLM.svg")
    await ctx.response.send_message(embed=embed)


@bot.tree.command(
    name="fakeid",
    description="Génère une fausse identité pour vous inscrire sur des sites par exemple"
)
async def fakeid(ctx):
    fakeidentity = fakeidy.fakeidy()
    embed = discord.Embed(title="Nouvelle identité générée", colour=0x6e00f5, description=fakeidentity,
                          timestamp=datetime.datetime.now())
    embed.set_thumbnail(url="https://cdn.onelots.fr/u/4ZW8nv.jpg")
    embed.set_footer(text="With ❤️ by Mathis & Roch", icon_url="https://cdn.onelots.fr/u/EQndLM.svg")
    await ctx.response.send_message(embed=embed)


@bot.tree.command(
    name="insulte",
    description="Génère une insulte plus ou moins polie"
)
async def insulte(ctx):
    insult = insulta.generateInsulte()
    await ctx.response.send_message(insult)


@bot.tree.command(
    name="addinsulte",
    description="Ajoute une insulte à la liste",
)
async def addinsulte(ctx: commands.Context, insulte: str):
    result = insulta.addinsulte(ctx, insulte)
    await ctx.response.send_message(result)


@bot.tree.command(
    name="nasa",
    description="Envoie une image aléatoire de la NASA"
)
async def nasa(ctx):
    image = nasapi.nasa()
    embed = discord.Embed(colour=0x691b93, description=f"Voici une image aléatoire de la NASA : ")
    embed.set_image(url=image)
    try:
        await ctx.response.send_message(embed=embed)
    except Exception as e:
        await ctx.response.send(nasa)


@bot.tree.command(
    name="earth",
    description="Envoie une image aléatoire de la Terre"
)
async def earth(ctx):
    image = earthapi.earth()
    embed = discord.Embed(colour=0x691b93, description=f"Voici une image aléatoire de la Terre : ")
    file = discord.File(image, filename="image.jpg")
    embed.set_image(url="attachment://image.jpg")
    try:
        await ctx.response.send_message(embed=embed, file=file)
    except Exception as e:
        await ctx.response.send(earth)


@bot.tree.command(
    name="roulette",
    description="Lance une partie de roulette russe.... attention, si vous perdez, vous êtes kick !",
)
async def roulette(ctx):
    result = rouletteapi.roulette()
    print(ctx.user.id)
    emoji_death = bot.get_emoji(1213495608464248832)
    emoji_life = str(bot.get_emoji(1213495661710807040))
    if result:
        embed = discord.Embed(colour=0x691b93, description=f"{emoji_death} | BANG ! Vous avez perdu !", timestamp=datetime.datetime.now())
        embed.set_author(name="Roulette Russe")
        embed.set_thumbnail(url="https://cdn.onelots.fr/u/VwRaYK.jpg")
        embed.set_footer(icon_url="https://cdn.onelots.fr/u/4ZW8nv.jpg")
        user = ctx.guild.get_member(ctx.user.id)
        try:
            await ctx.response.send_message(embed=embed)
        except Exception as e:
            await ctx.response.send("nickel ça marche pas")
        await user.send(f"Tu es décédé, et tu as été kick du serv.... Pour le rejoindre, c'est ici : https://discord.gg/bfXvSgTa2n")
        await user.send(emoji_death)
        await user.send("Gros nullos")
        await user.kick(reason=f"{emoji_death} | Tu es mort...... RIP")
    else:
        embed = discord.Embed(colour=0x691b93, description=f"{emoji_life} | Clic..... Vous avez survécu !", timestamp=datetime.datetime.now())
        embed.set_author(name="Roulette Russe")
        embed.set_thumbnail(url="https://cdn.onelots.fr/u/VwRaYK.jpg")
        embed.set_footer(icon_url="https://cdn.onelots.fr/u/4ZW8nv.jpg")
        try:
            await ctx.response.send_message(embed=embed)
        except Exception as e:
            await ctx.response.send("nickel ça marche pas")




@bot.event
async def on_ready():
    channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))
    channel = bot.get_channel(channel_id)
    if channel:  # Vérifie si le canal a été trouvé
        await channel.send("Restarted • 🔃")
    else:
        print(f"Error : Canal with ID {channel_id} not found.")
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Game(name="🐋Dockerized by Zerteur🤖"), status=discord.Status.online)
    await getNextOpening.start()


@tasks.loop(minutes=10.0)
async def getNextOpening():
    getNextOpening = pont_chaban.getNextHourOpen()
    if (getNextOpening[0]):
        await pont_chaban.openingNOW(getNextOpening[1])
