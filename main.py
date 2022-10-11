from PIL import Image
import os, sys
import shutil
import time

def convert_to_jpg(infile):
    try:
        shutil.rmtree('Converted IMGs')
    except Exception as e:
        print(e)


    os.mkdir('/Users/arymehr/Documents/CS Projects/Image Resizing/Converted IMGs')

    removed_filetype = ''.join(infile.split('.')[:-1])
    outfile = f"Converted IMGs/{removed_filetype}.jpg"
    
    if infile != outfile:
        try:
            with Image.open(infile) as to_jpg:
                rgb_im = to_jpg.convert('RGB')
                rgb_im.save(outfile)
        except Exception as e:
            print(e)






convert_to_jpg('testim.png')
