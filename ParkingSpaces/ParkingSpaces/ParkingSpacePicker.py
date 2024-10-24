import pickle

import cv2

img = cv2.imread('carParkImg.png')
width, height = 107, 48
posList = []


def mouseClick(events, x, y, flags, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if pos[0] < x < pos[0] + width and pos[1] < y < pos[1] + height:
                posList.pop(i)

    with open('CarParkPos','wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('carParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)
