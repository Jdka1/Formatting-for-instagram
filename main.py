from scripts.createpost import create_post
from PIL import Image


imgpath = "/Users/aryanmehra/Downloads/4V7A3707.jpg"
topic = "landscapephotography"
numtags = 10


with Image.open(imgpath) as f:
    create_post(
        topic=str(topic),
        numtags=numtags,
        imgpath=imgpath
    )