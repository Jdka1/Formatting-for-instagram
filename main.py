from PIL import Image
import os, sys
import shutil
import time

def convert_to_jpg(infile, portrait):
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
                print(rgb_im.size)
                rgb_im.thumbnail((1080, 1350)) #if portrait == True else rgb_im.thumbnail((1080, 566))
                rgb_im.show()
                # rgb_im.save(outfile.resize())
                

                for i in range(1, 100, 5):
                    rgb_im.save(outfile, quality=i)
        except Exception as e:
            print(e)






convert_to_jpg('testim.png', portrait=True)
