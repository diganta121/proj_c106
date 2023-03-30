import cv2

img = cv2.imread("abc.jpeg")
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray)      # scaleFartor(1.1- 1.9) ,minNeighbor()
print(faces)
i = 0

for (x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       roi_img = img[y:y+h,x:x+w]
       cv2.imwrite(f"face{i}.jpg",roi_img)
       i+=1
cv2.imshow('img',img)
cv2.waitKey(0)
