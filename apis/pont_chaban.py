import cloudscraper
import datetime
import locale

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
    return (0)