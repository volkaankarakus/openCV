# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 00:40:34 2021

@author: VolkanKarakuş
"""
#%% LANCZOS
import glob
from PIL import Image

files = glob.glob ("*.jpg")
basewidth = 500
for i in files :
    
    
    img = Image.open(i)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    if hsize>=basewidth:
        img = img.resize((basewidth, hsize), Image.LANCZOS)
        img.save('Resized{}.jpg'.format(i))
        
    else:
        continue

#%% Delete old images
import glob
import os 
import cv2


files = glob.glob ("*.jpg")
for each in files:
    img=cv2.imread(each)
    if each[0]!='R':
        os.remove(each)
        
