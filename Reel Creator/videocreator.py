from moviepy.editor import *
import os

print('\n'*10)



before, after = "Reel Creator/Photos/4V7A0160-2.jpg", "Reel Creator/Photos/4V7A0160.jpg"


clips = [ImageClip(before).set_duration(2) ,
         ImageClip(after).set_duration(2)]

reel = concatenate_videoclips(clips, method="compose")
reel.write_videofile("Video Creator/reel.mp4", fps=24)