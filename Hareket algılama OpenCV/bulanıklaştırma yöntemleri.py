import cv2 as c
import numpy  as np

camera = c.VideoCapture(0)

while True:
    
    r, img=camera.read()
    
    hsv=c.cvtColor(img, c.COLOR_BGR2HSV)
    img_gri = c.cvtColor(img, c.COLOR_BGR2GRAY)
    
    mask=c.inRange(hsv, (0,100,30), (10,255,255))
    img_masked=c.bitwise_and(img, hsv,mask=mask)
    
    
    kernel=np.ones((15,15), np.float32)/225
    smoothed=c.filter2D(img_masked , -1, kernel) #filtreleme işlemi
    
    
    c.imshow("real window", img)
    c.imshow("smoothed", smoothed)
    c.imshow("masked", img_masked)
    
    
    
    
    
    
    if c.waitKey(20) & 0xFF==ord("q"):
        break

camera.release()
c.destroyAllWindows()
