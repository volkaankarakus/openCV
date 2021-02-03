# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:16:48 2021

@author: VolkanKarakuş
"""

import cv2
import os
from glob import glob
#%% from PNG to JPG
png=glob("‪D:\pngFolder\*.png")

for each in png:
    img=cv2.imread(each)
    cv2.imwrite(each[:-3]+"jpg",img)
    os.remove(each)
    
#%% from BMP to JPG
png=glob("‪D:\bmpFolder\*.bmp")

for each in png:
    img=cv2.imread(each)
    cv2.imwrite(each[:-3]+"jpg",img)
    os.remove(each)

#%% from  JPEG to JPG
jpeg=glob("‪D:\jpegFolder\*.jpeg")

for each in png:
    img=cv2.imread(each)
    cv2.imwrite(each[:-4]+"jpg",img)
    os.remove(each)
    
#%% from TIFF to JPG
tiff=glob("‪D:\tiffFolder\*.jpeg")

for each in png:
    img=cv2.imread(each)
    cv2.imwrite(each[:-4]+"jpg",img)
    os.remove(each)