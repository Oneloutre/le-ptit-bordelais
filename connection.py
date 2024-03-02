from discord.ext import commands, tasks
import discord
import apis.pont_chaban as pont_chaban
import datetime
import apis.fakeid as fakeidy
import apis.insulte as insulta
import cloudscraper
import apis.nasa as nasapi
import apis.earth as earthapi
import apis.russianRoulette as rouletteapi

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
    embed = discord.Embed(title="Nouvelle identité générée", colour=0x6e00f5, description=fakeidentity, timestamp=datetime.datetime.now())
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

async def addinsulte(ctx : commands.Context, insulte : str):
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
    if result:
        embed = discord.Embed(colour=0x691b93, description=f"BANG ! Vous avez perdu !")
        user = ctx.guild.get_member(ctx.user.id)
        await user.kick(reason="Tu es mort...... RIP")
    else:
        embed = discord.Embed(colour=0x691b93, description=f"Clic..... Vous avez survécu !")
    try:
        await ctx.response.send_message(embed=embed)
    except Exception as e:
        await ctx.response.send("nickel ça marche pas")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('Bonjour'):
        await message.channel.send('Salut')
    if message.author != bot.user:
        with open(f"logs.txt", "a") as file:
            file.write(f"{message.author} : {message.content}\n")
    await bot.process_commands(message)

@bot.event
async def on_ready():
    await bot.get_channel(1213023082197946418).send("Redémarré • 🔃")
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Game(name="Scraper MY BOI"), status=discord.Status.online)
    await getNextOpening.start()



@tasks.loop(minutes=10.0)
async def getNextOpening():
    getNextOpening = pont_chaban.getNextHourOpen()
    if(getNextOpening[0]):
        await pont_chaban.openingNOW(getNextOpening[1])




