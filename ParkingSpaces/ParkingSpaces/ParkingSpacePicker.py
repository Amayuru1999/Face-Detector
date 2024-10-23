import cv2

img = cv2.imread('carParkImg.png')
width,height=107,48
posList=[]

def MouseClick

while True:
    cv2.rectangle(img,(50,192),(157,240),(255,0,255),2)
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", MouseClick)
    cv2.waitKey(1)