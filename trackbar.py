import cv2
import numpy as np

def nothing(x):
    pass

canvas=np.zeros((512,512,3),dtype=np.uint8)
#olusturdugumuz pencereye ad verelim
cv2.namedWindow("image")#bunu yapmamizin nedeni trackbar arayuzunu rengini degistirecegimiz pencereye yerlestirecegimizi belirmek.

#renk,bulunacagi pencere,baslangic ve bitis degerleri,bos fonksiyon
cv2.createTrackbar("R","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)

#anahtari olustur.
switch="0: OFF,1: ON"
cv2.createTrackbar(switch,"image",0,1,nothing)

#trackbarlardan alinan degerleri pencereye yansit.
while True:
    cv2.imshow("image",canvas)
    if cv2.waitKey(1)==27:
        break
    r=cv2.getTrackbarPos("R","image")
    g=cv2.getTrackbarPos("G","image")
    b=cv2.getTrackbarPos("B","image")
    s=cv2.getTrackbarPos(switch,"image")
    if s==0:
        canvas[:]=[0,0,0]
    if s==1:
        canvas[:]=[b,g,r]

cv2.destroyAllWindows()
