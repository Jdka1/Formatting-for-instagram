from PIL import Image
import os, sys
import shutil
import time


def convert_to_jpg(infile, outfile):
    try:
        shutil.rmtree('Converted IMGs')
    except Exception:
        pass

    sys.path.insert(0, "/Users/aryanmehra/Documents/CS Projects/Instagram-bot/")
    os.mkdir('Converted IMGs/')

    removed_filetype = ''.join(infile.split('.')[:-1])
    
    try:
        with Image.open(infile) as to_jpg:
            rgb_im = to_jpg.convert('RGB')
            rgb_im.thumbnail((1280, 1080)) # limiting width and height to 1080p
            rgb_im.save(outfile)

    except Exception as e:
        print(e)