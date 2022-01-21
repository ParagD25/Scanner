import cv2
import numpy as np

capture=cv2.VideoCapture(0)

def basic(frame):

    frameG=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameBlur=cv2.GaussianBlur(frameG,(7,7),1)
    frameCanny=cv2.Canny(frameBlur,150,150)

    kernel=np.ones((7,7))

    frameDilate=cv2.dilate(frameCanny,kernel,iterations=2)
    frameErode=cv2.erode(frameDilate,kernel,iterations=1)

    return frameErode

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)

        if area>2500:
            cv2.drawContours(frame2,cnt,-1,(255,0,0),3)

            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            objcor=len(approx)

            x,y,w,h=cv2.boundingRect(approx)


while True:
    ret,frame=capture.read()
    frame2=frame.copy()

    myFrame=basic(frame)

    cv2.imshow('Result',myFrame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()