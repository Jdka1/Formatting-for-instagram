from scripts.createpost import create_post
from PIL import Image

imgpath = str(input('Enter Filepath: '))
topic = str(input('Enter hashtag topic: '))
numtags = int(input('Enter number of hashtags: '))


with Image.open(imgpath) as f:
    create_post(
        topic=str(topic),
        numtags=numtags,
        imgpath=imgpath
    )
