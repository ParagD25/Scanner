import cv2
import numpy as np

capture=cv2.VideoCapture(0)

imgW=550
imgH=670

capture.set(3,640)
capture.set(4,480)

def basic(frame):

    frameG=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameBlur=cv2.GaussianBlur(frameG,(7,7),1)
    frameCanny=cv2.Canny(frameBlur,150,150)

    kernel=np.ones((7,7))

    frameDilate=cv2.dilate(frameCanny,kernel,iterations=2)
    frameErode=cv2.erode(frameDilate,kernel,iterations=1)

    return frameErode

def getContours(img):

    largest=np.array([])
    areaMax=0
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)

        if area>2500:
            cv2.drawContours(frame2,cnt,-1,(255,0,0),3)

            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            
            if area>areaMax and len(approx)==4:
                largest=approx
                areaMax=area

    return largest

def warpCorrected(points):
    points=points.reshape((4,2))

    newPoints=np.zeros((4,1,2),np.int32)

    addPointVal=points.sum(1)

    newPoints[0]=points[np.argmin(addPointVal)]
    newPoints[3]=points[np.argmax(addPointVal)]

    diffPointVal=np.diff(points,axis=1)

    newPoints[1]=points[np.argmin(diffPointVal)]
    newPoints[2]=points[np.argmax(diffPointVal)]

    return newPoints

def warp(frame,scanArea):

    scanArea=warpCorrected(scanArea)
    
    point1=np.float32(scanArea)
    point2=np.float32([[0,0],[imgW,0],[0,imgH],[imgW,imgH]])

    matrix=cv2.getPerspectiveTransform(point1,point2)

    imgScan=cv2.warpPerspective(frame,matrix,(imgW,imgH))

    return imgScan


while True:
    ret,frame=capture.read()
    frame2=frame.copy()

    myFrame=basic(frame)
    scanArea=getContours(myFrame)

    if scanArea.size!=0:
        imgOutput=warp(frame,scanArea)
        
        cv2.imshow('Scanned Paper',imgOutput)
        cv2.imshow('Scanned Paper Outline',frame2)

    else:
        cv2.imshow('Scanned Paper',frame)
        cv2.imshow('Scanned Paper Outline',frame)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()