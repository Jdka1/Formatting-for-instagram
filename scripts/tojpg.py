from PIL import Image
import os, sys
import shutil
import time


def convert_to_jpg(infile):
    try:
        shutil.rmtree('Converted IMGs')
    except Exception:
        pass

    sys.path.insert(0, "/Users/aryanmehra/Documents/CS Projects/Formatting-for-instagram/")
    os.mkdir('Converted IMGs/')

    removed_filetype = ''.join(infile.split('.')[:-1])
    outfile = f"Converted IMGs/tojpg.jpg"
    
    if infile != outfile:
        try:
            with Image.open(infile) as to_jpg:
                rgb_im = to_jpg.convert('RGB')
                rgb_im.thumbnail((1080, 1080)) # limiting width and height to 1080p
                rgb_im.save(outfile)

        except Exception as e:
            print(e)