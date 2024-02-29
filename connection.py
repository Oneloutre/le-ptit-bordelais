from discord.ext import commands, tasks
from discord.ui import Button
import discord
import apis.pont_chaban as pont_chaban
import datetime

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.tree.command(
    name="pont",
    description="Une commande pour se tenir au courant du lever de pont (et éviter les retards d'Alexis et Mathis)"
)

async def pont(ctx):
    nextBoat = pont_chaban.getAllBoat()
    embed = discord.Embed(title="Lien de l'api utilisée", url="https://opendata.bordeaux-metropole.fr/explore/dataset/previsions_pont_chaban/api/", colour=0x00b0f4,
                          description=f"Voilà les prochaines dates auxquelles le pont chaban sera inaccessible.\n\n**{nextBoat[0][1]} | __{nextBoat[0][0]}__:**\n__Fermeture__ : {nextBoat[0][2]}\n__Ouverture__ :{nextBoat[0][3]}\n ---------------------------- \n"
                                      f"\n**{nextBoat[1][1]} | __{nextBoat[1][0]}__ :**\n__Fermeture__ : {nextBoat[1][2]}\n__Ouverture__ :{nextBoat[1][3]}\n ---------------------------- \n"
                                      f"\n**{nextBoat[2][1]} | __{nextBoat[2][0]}__ :**\n__Fermeture__ : {nextBoat[2][2]}\n__Ouverture__ :{nextBoat[2][3]}\n ---------------------------- \n"
                                      f"\n**{nextBoat[3][1]} | __{nextBoat[3][0]}__ :**\n__Fermeture__ : {nextBoat[3][2]}\n__Ouverture__ :{nextBoat[3][3]}\n ---------------------------- \n"
                                      f"\n**{nextBoat[4][1]} | __{nextBoat[4][0]}__ :**\n__Fermeture__ : {nextBoat[4][2]}\n__Ouverture__ :{nextBoat[4][3]}\n ---------------------------- \n")
    embed.set_author(name="Levée et fermeture du pont Chaban")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Logo_Efrei_2022.svg/512px-Logo_Efrei_2022.svg.png")
    embed.set_image(url="https://passion-aquitaine.ouest-france.fr/wp-content/uploads/2018/02/chaban-bassins-flot.jpg")
    await ctx.response.send_message(embed=embed)
    print(nextBoat)

@bot.tree.command(
    name="aide",
    description="Pour connaitre toutes les commandes à utiliser"
)

async def aide(ctx):
    embed = discord.Embed(title="Github du bot",
                      url="https://github.com/oneloutre",
                      description="__Liste des commandes :__\n\n• /pont : affiche les prochaines levées du pont\n**--------------------------------**\n\n• /aide : Affiche ce menu",
                      colour=0xf500ed,
                      timestamp=datetime.datetime.now())
    embed.set_author(name="Liste des commandes disponibles")
    embed.set_thumbnail(url="https://cdn.onelots.fr/u/4ZW8nv.jpg")
    embed.set_footer(text="With ❤️ by Mathis & Roch", icon_url="https://cdn.onelots.fr/u/EQndLM.svg")
    button = Button(label="/pont", style=discord.ButtonStyle.blurple)
    #button.callback = pont()
    view = discord.ui.View()
    view.add_item(button)

    await ctx.response.send_message(embed=embed, view=view)

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
    await bot.change_presence(activity=discord.Game(name="Scraper MY BOI"), status=discord.Status.online)
    await bot.get_channel(1212154817355710474).send("Redémarré • 🔃")
    await getNextOpening.start()


@tasks.loop(minutes=10.0)
async def getNextOpening():
    getNextOpening = pont_chaban.getNextHourOpen()
    if(getNextOpening[0]):
        await openingNOW(getNextOpening[1])

    
