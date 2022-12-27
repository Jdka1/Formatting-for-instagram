from scripts.createpost import create_post
from PIL import Image
from instabot import Bot
import time
import random
import shutil

from dotenv import load_dotenv
import os

def delete_config():
    try:
        shutil.rmtree('config')
    except Exception:
        pass


def pause_random():
    time.sleep(random.uniform(2,3))


def post_to_insta():
    if (input("Should this be posted? (y/n) ") != 'y'):
        return
    if (input("Confirm (y/n) ") != 'y'):
        return
    
    print("Posting...")
    
    load_dotenv()
    
    delete_config()
 
    bot = Bot()
    bot.login(username=os.getenv("USERNAME"),
            password=os.getenv("PASSWORD"))
    
    pause_random()
    with open("Post Info/caption.txt", "r") as f:
        bot.upload_photo("Post Info/tojpg.jpg", caption=f.read())
        
        
    pause_random()
    
    
    



# travelphotography
topics = ["travelphotography"]
numtags = 30
imgpath = ""
with Image.open(imgpath) as f:
    create_post(
        topics=topics,
        numtags=numtags,
        imgpath=imgpath
    )

post_to_insta()
