import cv2 as c
from datetime import datetime


def imageDiff(img0,img1,img2):
    
    diff1=c.absdiff(img2, img1)
    diff2=c.absdiff(img1, img0)
    return c.bitwise_and(diff1, diff2)


camera = c.VideoCapture(0)
treshold = 90000 #define a treshold.its a kind of sensetive adapter.

img_before = c.cvtColor(camera.read()[1], c.COLOR_BGR2GRAY)
img_now = c.cvtColor(camera.read()[1] , c.COLOR_BGR2GRAY)
img_after = c.cvtColor(camera.read()[1] , c.COLOR_BGR2GRAY)

timeControl = datetime.now().strftime("%Ss")

while True:
    c.imshow("myWindow", camera.read()[1])
    if c.countNonZero(imageDiff(img_before , img_now, img_after)) > treshold and datetime.now().strftime("%Ss") != timeControl:
        c.imwrite(datetime.now().strftime("%Y %m %d _ %Hh %Mm %Ss")+".png", camera.read()[1])
    
    timeControl=datetime.now().strftime("%Ss")
    
    img_before=img_now
    img_now=img_after
    img_after = c.cvtColor(camera.read()[1], c.COLOR_BGR2GRAY)
    
    if c.waitKey(15) & 0xFF==ord("q"):
        break
    
camera.release()
c.destroyAllWindows()
    
