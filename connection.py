from discord.ext import commands, tasks
import discord
import apis.pont_chaban as pont_chaban
import datetime
import apis.fakeid as fakeidy

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.tree.command(
    name="pont",
    description="Une commande pour se tenir au courant du lever de pont (et éviter les retards d'Alexis et Mathis)"
)


async def pont(ctx):
    embed = pont_chaban.SendPont()
    await ctx.response.send_message(embed=embed)


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


async def openingNOW(time, ctx):
    embed = discord.Embed(title="Lien de l'api utilisée", url="https://opendata.bordeaux-metropole.fr/explore/dataset/previsions_pont_chaban/api/", colour=0x00b0f4,
                          description=f"**Attention, le pont va bientôt s'ouvrir dans {time} minutes !!!!!!**")
    embed.set_author(name="Levée et fermeture du pont Chaban")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Logo_Efrei_2022.svg/512px-Logo_Efrei_2022.svg.png")
    embed.set_image(url="https://passion-aquitaine.ouest-france.fr/wp-content/uploads/2018/02/chaban-bassins-flot.jpg")
    await ctx.response.send_message(embed=embed)


@bot.event
async def on_ready():
    await bot.tree.sync()
    await bot.get_channel(1213023082197946418).send("Redémarré • 🔃")
    await bot.change_presence(activity=discord.Game(name="Scraper MY BOI"), status=discord.Status.online)
    await getNextOpening.start()


@tasks.loop(minutes=10.0)
async def getNextOpening():
    getNextOpening = pont_chaban.getNextHourOpen()
    if(getNextOpening[0]):
        await openingNOW(getNextOpening[1])




