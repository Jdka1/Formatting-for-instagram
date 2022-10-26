from moviepy.editor import *

print('\n'*10)

clips = [ImageClip("Post Info/tojpg.jpg").set_duration(2) ,
         ImageClip("Post Info/Screen Shot 2021-11-23 at 5.03.04 PM.png").set_duration(2)]

reel = concatenate_videoclips(clips, method="compose")
reel.write_videofile("Video Creator/reel.mp4", fps=24)