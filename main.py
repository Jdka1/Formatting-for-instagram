from PIL import Image
import os, sys


def convert_to_jpg(infile):
    os.mkdir('/Users/arymehr/Documents/CS Projects/Image Resizing/')
    removed_filetype = ''.join(infile.split('.')[:-1])
    outfile = f"{removed_filetype}.jpg"
    

    if infile != outfile:
        try:
            with Image.open(infile) as to_jpg:
                rgb_im = to_jpg.convert('RGB')
                rgb_im.save(outfile)
        except Exception as e:
            print(e)






convert_to_jpg('testim.png')
