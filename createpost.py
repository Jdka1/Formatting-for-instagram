from scripts.gethashtags import get_hashtags
from scripts.tojpg import convert_to_jpg
import os
import shutil
from PIL import Image



def create_post(topic, numtags, imgpath):
    try:
        shutil.rmtree('post info')
    except Exception:
        pass

    os.mkdir('/Users/arymehr/Documents/CS Projects/Formatting-for-instagram/Post Info')

    # create caption
    with open('Post Info/caption.txt', 'w') as f:
        hashtags = get_hashtags(topic, numtags)
        formatted_hashtags = ''.join([f'{hashtag} ' for hashtag in hashtags])
        f.write(''.join(formatted_hashtags))


    # format image
    convert_to_jpg(imgpath)
    shutil.move("Converted IMGs/tojpg.jpg", "Post Info")




imgpath = str(input('Enter Filepath: '))
topic = str(input('Enter hashtag topic: '))
numtags = int(input('Enter number of hashtags: '))


with Image.open(imgpath) as f:
    create_post(
        topic=str(topic),
        numtags=numtags,
        imgpath=imgpath
    )