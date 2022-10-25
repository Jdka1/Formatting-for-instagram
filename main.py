from scripts.createpost import create_post
from PIL import Image
from credentials import creds
from instabot import Bot
import time
import random
import shutil


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
    
    delete_config()
 
    bot = Bot()
    bot.login(username=creds['user'],
            password=creds['pass'])
    
    pause_random()
    with open("Post Info/caption.txt", "r") as f:
        bot.upload_photo("Post Info/tojpg.jpg", caption=f.read())
        
        
    pause_random()
    
    
    




# topics = ["sanfranciscophotography"]
# numtags = 30
# imgpath = "/Users/aryanmehra/Downloads/IMG_0545 (1).jpg"

# with Image.open(imgpath) as f:
#     create_post(
#         topics=topics,
#         numtags=numtags,
#         imgpath=imgpath
#     )

# post_to_insta()

bot = Bot()
bot.login(username=creds['user'],
        password=creds['pass'])

latest_post_id = bot.get_your_medias()[0]
print(latest_post_id)

bot.comment(latest_post_id, "🌉🌉")

