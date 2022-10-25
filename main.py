from scripts.createpost import create_post
from PIL import Image


topics = ["landscapephotography","alaska","snow"]
numtags = 20
imgpath = "/Users/aryanmehra/Downloads/4V7A3707.jpg"

with Image.open(imgpath) as f:
    create_post(
        topics=topics,
        numtags=numtags,
        imgpath="/Users/aryanmehra/Downloads/4V7A3707.jpg"
    )