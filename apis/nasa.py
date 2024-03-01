from datetime import datetime as date
import random
import cloudscraper

requests = cloudscraper.create_scraper()
def nasa():

    # Générez une date aléatoire entre la date de début de l'API (16 juin 1995) et aujourd'hui
    date_debut = date(1995, 6, 16)
    date_fin = date.today()
    date_aleatoire = date.fromordinal(random.randint(date_debut.toordinal(), date_fin.toordinal()))

    # Formattez la date au format YYYY-MM-DD
    date_formattee = date_aleatoire.strftime('%Y-%m-%d')

    # URL de l'API APOD de la NASA pour obtenir une image aléatoire
    url = f'https://api.nasa.gov/planetary/apod?api_key=TyjlXs81lWtDja06eb0T3NHcXwrjpPjVII2OTyhT&date={date_formattee}'

    try:
        # Effectuez une requête GET à l'API
        response = requests.get(url)

        # Vérifiez si la requête a réussi (code de statut HTTP 200)
        if response.status_code == 200:
            data = response.json()
            # Récupérez l'URL de l'image
            image_url = data['url']
            return(image_url)
        else:
            return(f"Échec de la requête : Code de statut {response.status_code}")
    except Exception as e:
        return(f"Une erreur s'est produite : {e}")