import cloudscraper
import random
import datetime

jour_actuel = datetime.datetime.now().day
requests = cloudscraper.create_scraper()


def insulta():
    url = "https://evilinsult.com/generate_insult.php?lang=fr&type=json"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            insult = data["insult"]
            return(insult)
        else:
            return(f"Échec de la requête : Code de statut {response.status_code}")
    except Exception as e:
        return(f"Une erreur s'est produite : {e}")


def generateInsulte():
    randomnumber = random.randint(1, 8)
    if randomnumber < 8:
        with open("Assets/insultes.txt", "r") as file:
            insultes = file.readlines()
            biginsulte = insultes[random.randint(0, len(insultes))]
            return(biginsulte)
    else:
        return(insulta())



def addinsulte(ctx, insulte):
    with open("Assets/insultes.txt", "a") as file:
        file.write(insulte + "\n")
        reponse = "Je retiens...\"" + insulte + "\" a été ajouté à la liste des insultes."
        print(insulte + " a été ajouté à la liste des insultes")
    return reponse