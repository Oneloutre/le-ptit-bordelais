![banner](Assets/banner.png)

---

![GitHub license](https://img.shields.io/github/license/oneloutre/le-ptit-bordelais) ![GitHub last commit](https://img.shields.io/github/last-commit/oneloutre/le-ptit-bordelais)![language](https://img.shields.io/badge/language-python-blue) ![GitHub repo size](https://img.shields.io/github/repo-size/oneloutre/le-ptit-bordelais) ![Made with love](https://img.shields.io/badge/%E2%9D%A4%EF%B8%8F_Made_with-love-red) 

# BOT DISCORD Le P'tit Bordelais Readme

## 🔍 Retrieving the LPB bot image for Docker
You can find the LPB bot image for Docker [here](https://hub.docker.com/r/lzerteur/lpb).

## 🐳 Docker Run Command
To run the bot with Docker, execute the following command:
```
docker run -e BOT_TOKEN=<YOUR_DISCORD_TOKEN> -d --name <RUNNING_NAME> lzerteur/lpb:<TAG>
```

## 🐳 Docker Compose Configuration
Alternatively, you can use Docker Compose. Add the following to your `docker-compose.yml` file:
```
version: '3.8'
services:
  mon_service:
    image: lzerteur/lpb:<TAG>
    environment:
      BOT_TOKEN: "<YOUR_DISCORD_TOKEN>"
    restart: unless-stopped
```

## 💬 Command Guide
If you want to interact with the bot, here are the available commands:

- 🌉 | `/pont` : Display upcoming bridge openings
- 👤 | `/fakeid` : Generate a fake identity
- 🤬 | `/insulte` : Generate a more or less polite insult
- 🗣️ | `/addinsulte [insulte]` : Add an insult to the list
- 🚀 | `/nasa` : Send a random image from NASA
- 🌍 | `/earth` : Send a random image of Earth
- 🔫 | `/roulette` : Play a game of Russian roulette... beware, if you lose, you get kicked!

For more information, type:
```
ℹ️ | /aide : Display this menu
```

Enjoy interacting with LPB bot! 🤖
