import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('1.jpeg')

grayscaled_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates= trained_face_data.detectMultiScale(grayscaled_img)


(x,y,w,h)=face_coordinates[0]
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

print(face_coordinates)

cv2.imshow('Face Detector', img)
cv2.waitKey()

print("Code completed 🚀")