import cv2

cap = cv2.VideoCapture('carPark.mp4')

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    cv2.imshow("Video", img)
    cv2.waitKey(1)
