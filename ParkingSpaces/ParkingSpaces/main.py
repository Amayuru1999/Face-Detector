import pickle

import cv2

width, height = 107, 48
cap = cv2.VideoCapture('carPark.mp4')

with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)


def checkParkingSpace():
    for pos in posList:
        x,y = pos

        imgCrop = img[y:y + height, x:x + width]
        cv2.imshow(str(x*y), imgCrop)



while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur =cv2.GaussianBlur(imgGray,(3,3),1)

    checkParkingSpace()
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Video", img)
    cv2.imshow("Blur", imgBlur)
    cv2.waitKey(10)
