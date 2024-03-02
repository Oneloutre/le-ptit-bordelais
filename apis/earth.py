import random
import cloudscraper
import json

requests = cloudscraper.create_scraper()

def earth():
    allKeyFile = open("./apis/listIndexImageearth.json")
    allKeyData = json.load(allKeyFile)
    
    key = random.choice(allKeyData["ids"])
    
    try :
        newImage = requests.get(f"https://www.gstatic.com/prettyearth/assets/data/v3/{key}.json")
        if newImage.status_code == 200:
            newImage = newImage.json()
            return requests.get(newImage["dataUri"])
        else:
            return(f"Échec de la requête : Code de statut {newImage.status_code}")
    except Exception as e:
        return(f"Une erreur s'est produite : {e}")