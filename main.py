import connection
import os
from dotenv import load_dotenv

dotenv = load_dotenv()
token = os.getenv('BOT_TOKEN')


if __name__ == "__main__":
    if not os.path.exists(".env"):
        print("Le fichier .env n'existe pas, veuillez le créer et y mettre le token du bot")
        token = str(input("Veuillez entrer le token du bot : "))
        with open(".env", "w") as file:
            file.write(f"BOT_TOKEN={token}")
    connection.bot.run(token)