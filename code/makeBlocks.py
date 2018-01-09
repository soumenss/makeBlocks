import numpy as np
import cv2
from PIL import Image
import math
import os
import glob


folder='F:/takeImage/'
savingfolder='E:/temp/blocked/'
imList=glob.glob(folder+'*.jpg')
blocksize=256

#img = Image.open('E:/temp/_MG_0524-01.jpeg')
n = 0

for imgname in imList:
    img = Image.open(imgname)
    (row, col) = img.size
    r = math.floor(row/blocksize)
    c = math.floor(col/blocksize)

    for i in range(r):
        up = i*blocksize
        for j in range(c):
            left = j*blocksize
            box=(left, up, left+blocksize, up+blocksize)
            crop = img.crop(box)
            n = n+1
            filename =savingfolder + str(n) + '.jpg'
            crop.save(filename)
