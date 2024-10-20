import cv2

img = cv2.imread('carParkImg.png')

while True:
    cv2.imshow("Image", img)
    cv2.waitKey(1)