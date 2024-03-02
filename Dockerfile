# Utiliser une image de base Python Alpine pour la construction et l'exécution
FROM python:3.12-alpine as builder

# Installer les dépendances dans un environnement virtuel
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'environnement virtuel dans notre image de base
FROM python:3.12-alpine
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

# Copier les fichiers nécessaires dans le conteneur
COPY ./apis /app/apis
COPY ./Assets /app/Assets
COPY ./connection.py /app/
COPY ./image.jpg /app/
COPY ./main.py /app/
COPY ./requirements.txt /app/

# Définir le répertoire de travail
WORKDIR /app

# Arguments de construction pour les variables d'environnement
ARG BOT_TOKEN
ARG DISCORD_CHANNEL_ID

# Créer un fichier .env avec les variables requises, générées dynamiquement à partir des arguments de construction
RUN echo "BOT_TOKEN=${BOT_TOKEN}" > .env && \
    echo "DISCORD_CHANNEL_ID=${DISCORD_CHANNEL_ID}" >> .env

# Créer un script de démarrage pour vérifier les variables d'environnement
RUN echo $'#!/bin/sh\n\
if [ -z "$BOT_TOKEN" ] || [ -z "$DISCORD_CHANNEL_ID" ]; then\n\
  echo "Erreur: Les variables BOT_TOKEN et DISCORD_CHANNEL_ID doivent être définies."\n\
  exit 1\n\
fi\n\
python main.py' > entrypoint.sh && chmod +x entrypoint.sh

# Utiliser le script comme point d'entrée
ENTRYPOINT ["sh", "entrypoint.sh"]
