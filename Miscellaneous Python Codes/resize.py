import Image
import os, sys

path = "test_round_2/"
dest_path = "resized/"
dirs = os.listdir( path )
dirs2 = os.listdir( dest_path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            print(item)
            im = Image.open(path+item)
            f, e = os.path.splitext(dest_path+item)
            imResize = im.resize((1024,1024), Image.ANTIALIAS)
            imResize.save(f, 'JPEG', quality=90)

resize()