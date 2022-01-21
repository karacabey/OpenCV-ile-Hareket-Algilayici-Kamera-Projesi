import cv2
import numpy as np

camera = cv2.VideoCapture(0) # 0 yazıldığı için bilgisayarın kendi kamerasını kullanır 
# eger bir videoyu işlemek istiyorsak o vidoenun path ini arguman olarak Videocapture fonkisyonuna
#göndermeliyiz

while 1: # sonsuz döngüde çalışıyoruz çunkü video filtreliyoruz... 
    
    ret, image=camera.read() # camerayı kullanuyoruz. ret değişkeni return iamge ise görüntü.
    
    
    ret = camera.set(3, 1024)  # piksel boyutları genişlik (with)
    ret = camera.set(3, 780)  # height (boyut) değişkeni 
    
    griton=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # gri tonlarında filtremizi oluşturuyoruz.
    
    cv2.imshow("window gray",griton) # gri tonlarını ayarladığımız window
    cv2.imshow("window", image) # cameradan aldığımız görüntüyü window adlı pencerede izliyoruz
    if cv2.waitKey(25) & 0xFF==ord("q"):# "q" tuşuna bastığımızda camerayı kapatıyoruz...
        break
    
camera.release() # camerayı kaaptıyoruz...
cv2.destroyAllWindows() # açık olan bütün pencereleri kapatıyoruz...
        
    


