from moviepy.editor import *
import os
import shutil
import sys

sys.path.insert(0, "/Users/aryanmehra/Documents/CS Projects/Formatting-for-instagram/")
from scripts.tojpg import convert_to_jpg



def create_clips():
    # Clear Photos folder and recreate it
    try:
        shutil.rmtree('Reel Creator/Photos')
    except Exception:
        pass

    os.mkdir('Reel Creator/Photos')


    # Convert before and after images to jpg and lower size
    before, after = "Reel Creator/4V7A0160-2.jpg", "Reel Creator/4V7A0160.jpg"
    convert_to_jpg(infile=before, outfile='Reel Creator/Photos/before.jpg')
    convert_to_jpg(infile=after, outfile="Reel Creator/Photos/after.jpg")





def create_reel():
    # Clear Reel folder and recreate it
    try:
        shutil.rmtree('Reel Creator/Reel')
    except Exception:
        pass

    os.mkdir('Reel Creator/Reel/')


    # # Create reel with before and after images
    clips = [ImageClip('Reel Creator/Photos/before.jpg').set_duration(2) ,
            ImageClip('Reel Creator/Photos/after.jpg').set_duration(2)]

    reel = concatenate_videoclips(clips, method="compose")
    reel.write_videofile("Reel Creator/Reel/reel.mp4", fps=24)





create_clips()
create_reel()

# bot.upload_video(file,caption)