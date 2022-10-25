from scripts.createpost import create_post
from PIL import Image
from credentials import creds
from instabot import Bot


def post_to_insta():
    if (input("Should this be posted? (y/n) ") != 'y'):
        return
    if (input("Confirm (y/n) ") != 'y'):
        return
    
    print("Posting...")
    
    
 
    bot = Bot()
    bot.login(username=creds['user'],
            password=creds['pass'])
    
    with open("Post Info/caption.txt", "r") as f:
        bot.upload_photo("Post Info/tojpg.jpg", caption=f.read())




topics = ["snowphotography"]
numtags = 30
imgpath = "/Users/aryanmehra/Downloads/4V7A3707.jpg"

with Image.open(imgpath) as f:
    create_post(
        topics=topics,
        numtags=numtags,
        imgpath="/Users/aryanmehra/Downloads/4V7A3707.jpg"
    )

# ----------------------------------------------------------

post_to_insta()

# add post to story as well