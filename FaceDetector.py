import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('1.jpeg')

grayscaled_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_coordinates= trained_face_data.detectMultiScale(grayscaled_img)
cv2.imshow('Face Detector', grayscaled_img)
cv2.waitKey()

print("Code completed 🚀")