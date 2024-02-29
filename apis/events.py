import cloudscraper
import datetime
import locale


def getEvents():
    URL = "https://opendata.bordeaux-metropole.fr/api/explore/v2.1/catalog/datasets/met_agenda/records?limit=5"
    scraper = cloudscraper.create_scraper()
    response = scraper.get(URL).json()

    Events = response['results']

    locale.setlocale(locale.LC_TIME, "fr_FR")
    #tabAllBoat = []

    #for i in range(len(Events)):
        #date = datetime.datetime.strptime(Events[i]["date_passage"], "%Y-%m-%d")
        #tabAllBoat.append([])
        #tabAllBoat[i].append(date.strftime('%d/%m/%Y'))
        #tabAllBoat[i].append(Events[i]['bateau'])
        #tabAllBoat[i].append(Events[i]['fermeture_a_la_circulation'])
        #tabAllBoat[i].append(Events[i]['re_ouverture_a_la_circulation'])
    return Events[]

print(getEvents())