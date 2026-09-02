# Reddit news bot for a Discord channel 
A simple Reddit Rich Site Summary (RSS) script to send the newest posts to a Discord webhook :)



## Features:

It sends the latest posts to a Discord webhook of your choice in the .env file, but I made this mostly for my own use 


## Requirements

- Feedparser 6.0.12
- Requests 2.34.2
- Python-dotenv 1.2.2

- <sub> or just use the requirements.txt file </sub>

## How to run?

Download the project folder, then change the urls in the .env file to your own Discord Webhook and your subreddit of choice,and then open the script on the background

On Linux:
```bash
nohup python discord-reddit-news-bot.py > logs.log 2>&1 &
```

On Windows:
```bash
pythonw discord-reddit-news-bot.py
```
