import os
import feedparser
import requests
import time
import logging
from dotenv import load_dotenv

load_dotenv()

global latest_post
latest_post = None

# Remember to fill the .env file with your urls otherwise it won't work
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")
SUBREDDIT_URL = os.getenv("PAGE_URL")


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'"
    }



# Calling the root logger
logger = logging.getLogger()
logging.basicConfig(filename = 'logs.log', encoding = 'utf-8', level = logging.INFO, format = "[%(levelname)s]  %(asctime)s | %(message)s")
logger.info("Opened the script")
print("Opened the script")



try:
    while True:
        try:
            response = requests.get(SUBREDDIT_URL, headers=header)
            feed = feedparser.parse(response.text)


            # Check to prevent a crash if the feedparser doesn't grab the page
            if feed.entries:

                latest_feed = feed.entries[0]
                
            else:
                # Cute print using the Godot structure, oh I feel nostalgia, I won't delete this comment
                #print("nos blokiaron los de: " + str(SUBREDDIT_URL_DBD) + ", bro")
                logger.error(f"Page empty")

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
                logger.info(f"Retrieving a new post: Title: {post_title}, Link: {post_link}")


            else:
            
                logger.info("Didn't find a new post")

            
        except Exception as error:

            logger.error("This is an error, something exploded along the way")

        
        time.sleep(30)

except KeyboardInterrupt:
    print("Closed the script")
    logger.info("Closed the script manually")
