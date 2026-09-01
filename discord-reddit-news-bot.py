import os
import feedparser
import requests
import time
import logging
from dotenv import load_dotenv

load_dotenv()

global latest_post
latest_post = None

# Remember to fill the .env file with the webhook to YOUR Discord channel
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

# Change the subreddit URL to whatever you want to see in your Discord Webhook (I like dead by daligght :) )
SUBREDDIT_URL = "https://www.reddit.com/r/deadbydaylight/new/.rss"


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'"
    }

print("Opened the script")

while True:
    try:
        response = requests.get(SUBREDDIT_URL, headers=header)
        feed = feedparser.parse(response.text)

        # Add a check here to avoid the app from crashing
        latest_feed = feed.entries[0]
        # Calling the root logger
        logger = logging.getLogger()
        logging.basicConfig(filename = 'logs.log', encoding = 'utf-8', level = logging.INFO, format = "[%(levelname)s]  %(asctime)s | %(message)s")


        # Check if it received all the entries
        if len(feed.entries) > 0:
            # The F stands for formatted, and the {} are a placeholder space for the text 
            logger.info(f"Title: {latest_feed.title}, Link: {latest_feed.link}, ID: {latest_feed.id}") 

        else:
            # Cute print using the Godot structure, oh I feel nostalgia
            #print("nos blokiaron los de: " + str(SUBREDDIT_URL_DBD) + ", bro")
            logger.error("Nothing found, the page is down or we did too many requests")

        post_title = latest_feed.title
        post_link = latest_feed.link
        post_id = latest_feed.id

        # The check to send the discord message if the ID is NOT the same
        if post_id != latest_post:
            
            # This is the message structure, you can change it to however you want
            # \n is a new line, Discord also supports bold text and italics with ** and * respectively
            discord_message = "**New Reddit post**\n" + "Link: " + post_link




            requests.post(WEBHOOK_URL, json={"content": str(discord_message)})
            latest_post = post_id
            logger.info("Found a new post, yummy")

        else:
            
            logger.info("Didn't find a new post")

    # Add a message upon closing the app
    #except KeyboardInterrupt:
        #logger.info("Closed the app manually")

    except Exception as error:

        logger.error("This is an error, something exploded along the way")

    time.sleep(30)