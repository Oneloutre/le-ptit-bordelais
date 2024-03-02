LPB Bot Readme

You can retrieve the LPB bot image for Docker here.

To run with Docker, use the following command:

docker run -e BOT_TOKEN=<YOUR_DISCORD_TOKEN> -d --name <RUNNING_NAME> lzerteur/lpb:<TAG>

Alternatively, you can use Docker Compose:

version: '3.8'
services:
  mon_service:
    image: lzerteur/lpb:<TAG>
    environment:
      BOT_TOKEN: "<YOUR_DISCORD_TOKEN>"
    restart: unless-stopped

If you want to interact with the bot, check out the command guide below:

🌉 | /pont : Display upcoming bridge openings
👤 | /fakeid : Generate a fake identity
🤬 | /insulte : Generate a more or less polite insult
🗣️ | /addinsulte [insulte] : Add an insult to the list
🚀 | /nasa : Send a random image from NASA
🌍 | /earth : Send a random image of Earth
🔫 | /roulette : Play a game of Russian roulette... beware, if you lose, you get kicked!

For more information, type:

ℹ️ | /aide : Display this menu

Enjoy interacting with LPB bot!
