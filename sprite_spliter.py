from PIL import Image
from itertools import product
import os
def tile(filename, width,height):
    cwd=os.getcwd()
    ndir=os.path.join(cwd,filename.split(".")[0]+"-SplitOutput")
    if not os.path.isdir(ndir):
        os.mkdir(ndir)
    img = Image.open(filename)
    size= img.size
    frames=width*height
    x=0
    y=0
    sizex=size[0]/width
    sizey=size[1]/height
    for i in range(0,frames):
        print(x,y)
        box = (x*sizex, y*sizey, (x+1)*sizex, (y+1)*sizey)
        img.crop(box).save(os.path.join(ndir,str(i)+os.path.basename(filename)))
        x+=1
        if x>width-1:
            x=0
            y+=1 

tile("test_image.png",6,5)
