from scripts.createpost import create_post
from PIL import Image 


imgpath = input('Enter Filepath: ')
hashtag_topic = input('Enter hashtag topic: ')
numtags = input('Enter number of hashtags: ')
with Image.open(imgpath) as f:
    create_post(
        topic=hashtag_topic,
        numtags=numtags,
        imgpath=imgpath
    )