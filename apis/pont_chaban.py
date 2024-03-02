import cloudscraper
import datetime
import locale
import discord

def getAllBoat():
    adress = "https://opendata.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/previsions_pont_chaban/records?order_by=date_passage%20ASC&limit=5&offset=3"
    scraper = cloudscraper.create_scraper()
    response = scraper.get(adress).json()

    allBoat = response['results']

    locale.setlocale(locale.LC_TIME, "fr_FR")
    tabAllBoat = []

    for i in range(len(allBoat)):
        date = datetime.datetime.strptime(allBoat[i]["date_passage"], "%Y-%m-%d")
        tabAllBoat.append([])
        tabAllBoat[i].append(date.strftime('%d/%m/%Y'))
        tabAllBoat[i].append(allBoat[i]['bateau'])
        tabAllBoat[i].append(allBoat[i]['fermeture_a_la_circulation'])
        tabAllBoat[i].append(allBoat[i]['re_ouverture_a_la_circulation'])

    return tabAllBoat

def getNextHourOpen():
    adress = "https://opendata.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/previsions_pont_chaban/records?order_by=date_passage%20ASC&limit=5&offset=3"
    scraper = cloudscraper.create_scraper()
    response = scraper.get(adress).json()

    nowTime = datetime.datetime.now()

    allBoat = response['results']

    locale.setlocale(locale.LC_TIME, "fr_FR")
    for i in allBoat:
        hour = datetime.datetime.strptime(i["fermeture_a_la_circulation"], "%H:%M").strftime('%H')
        date = datetime.datetime.strptime(i["date_passage"], "%Y-%m-%d")
        if (int(hour) - int(datetime.datetime.now().strftime('%H')) <= 2 and int(hour) - int(datetime.datetime.now().strftime('%H')) > 0) and date.strftime("%Y-%m-%d") == datetime.datetime.now().strftime("%Y-%m-%d"):
            return (1, (int(hour) - int(datetime.datetime.now().strftime('%H'))))
    return (0, 0)

def SendPont():
    nextBoat = getAllBoat()
    embed = discord.Embed(title="Lien de l'api utilisée", url="https://opendata.bordeaux-metropole.fr/explore/dataset/previsions_pont_chaban/api/", colour=0x00b0f4,
                          description=f"Voilà les prochaines dates auxquelles le pont chaban sera inaccessible.\n"
                                      f"\n**{nextBoat[0][1]} | __{nextBoat[0][0]}__:**\n__Fermeture__ : {nextBoat[0][2]}\n__Ouverture__ :{nextBoat[0][3]}\n ---------------------------- \n"
                                      f"\n**{nextBoat[1][1]} | __{nextBoat[1][0]}__ :**\n__Fermeture__ : {nextBoat[1][2]}\n__Ouverture__ :{nextBoat[1][3]}\n ---------------------------- \n"
                                      f"\n**{nextBoat[2][1]} | __{nextBoat[2][0]}__ :**\n__Fermeture__ : {nextBoat[2][2]}\n__Ouverture__ :{nextBoat[2][3]}\n ---------------------------- \n"
                                      f"\n**{nextBoat[3][1]} | __{nextBoat[3][0]}__ :**\n__Fermeture__ : {nextBoat[3][2]}\n__Ouverture__ :{nextBoat[3][3]}\n ---------------------------- \n"
                                      f"\n**{nextBoat[4][1]} | __{nextBoat[4][0]}__ :**\n__Fermeture__ : {nextBoat[4][2]}\n__Ouverture__ :{nextBoat[4][3]}\n ---------------------------- \n")
    embed.set_author(name="Levée et fermeture du pont Chaban")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Logo_Efrei_2022.svg/512px-Logo_Efrei_2022.svg.png")
    embed.set_image(url="https://passion-aquitaine.ouest-france.fr/wp-content/uploads/2018/02/chaban-bassins-flot.jpg")
    return embed


async def openingNOW(time, ctx):
    embed = discord.Embed(title="Lien de l'api utilisée", url="https://opendata.bordeaux-metropole.fr/explore/dataset/previsions_pont_chaban/api/", colour=0x00b0f4,
                          description=f"**Attention, le pont va bientôt s'ouvrir dans {time} minutes !!!!!!**")
    embed.set_author(name="Levée et fermeture du pont Chaban")
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Logo_Efrei_2022.svg/512px-Logo_Efrei_2022.svg.png")
    embed.set_image(url="https://passion-aquitaine.ouest-france.fr/wp-content/uploads/2018/02/chaban-bassins-flot.jpg")
    await ctx.response.send_message(embed=embed)

