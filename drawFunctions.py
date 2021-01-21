import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8)
#white
canvas+=255

cv2.line(canvas,(50,50),(400,400),(255,0,0),thickness=5) #blue
cv2.line(canvas,(50,400),(400,50),(0,255,0),thickness=5) #green
cv2.rectangle(canvas, (50,50), (400,400),(0,0,255),thickness=8)#red

#ici dolu dikdortgen icin thickness=-1 yapariz
cv2.rectangle(canvas, (20,20), (40,40),(240,120,156),thickness=-1)

#circle'da center,radius,color,thickness
cv2.circle(canvas,(225,225),40,(220,120,50),thickness=-1)

#triangle
p1=(100,100)
p2=(200,300)
p3=(120,40)
cv2.line(canvas,p1,p2,(20,120,120),thickness=2)
cv2.line(canvas,p2,p3,(80,100,170),thickness=2)
cv2.line(canvas,p3,p1,(30,120,220),thickness=2)

#herhangi bir sekil icin
points=np.array([[ [110,150], [240,320], [50,140], [145,128] ]],np.int32)
cv2.polylines(canvas,[points],True,(0,0,100),thickness=5) #cokgenin kapali olmasi icin true gir.

#elips icin merkez, yatay yaricap,dikey yaricap(genislik ve yukseklik), yatay eksenle yapacagi aci
cv2.ellipse(canvas,(160,160),(60,100),10,0,360,(255,0,0),thickness=2) #0dan 360a taradik,renk,thickness

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


