import cv2
import os
dataset = "dataset"


name = input("To create your face database \nPlease tell me your name :")

path = os.path.join(dataset,name)
if not os.path.isdir(path):
    os.makedirs(path)


width,height=130,100
alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)

count=1
while count < 31 :
    print(count)
    _,img = cam.read()
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),2)
        faceOnly = grayImg[y:y+h,x:x+h]
        resizeImg = cv2.resize(faceOnly,(width,height))
        cv2.imwrite("%s/%s.jpg" %(path,count),faceOnly)
        count+=1
    cv2.imshow("Creating Face Database",img)
    key = cv2.waitKey(10)
    if key == 27: #27 is for escape
        break
        
print(count,"Images Captured Successfully to recognise your face")

cam.release()
cv2.destroyAllWindows()
