from scripts.gethashtags import get_hashtags
from scripts.tojpg import convert_to_jpg
import os
import shutil
from PIL import Image



def create_post(topics, numtags, imgpath):
    try:
        shutil.rmtree('post info')
    except Exception:
        pass
    
    os.mkdir('Post Info/')

    # create caption
    with open('Post Info/caption.txt', 'w') as f:
        hashtags = get_hashtags(topics, numtags)
        formatted_hashtags = ''.join([f'{hashtag} ' for hashtag in hashtags])
        f.write(''.join(formatted_hashtags))


    # format image
    convert_to_jpg(imgpath, outfile="Converted IMGs/tojpg.jpg")
    shutil.move("Converted IMGs/tojpg.jpg", "Post Info")
