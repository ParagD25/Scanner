import cv2
import numpy as np

capture=cv2.VideoCapture(0)

imgW=480
imgH=640

capture.set(3,640)
capture.set(4,480)

count=1

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
            cv2.drawContours(frame2,cnt,-1,(35,255,0),2)

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

    imgCropped=imgScan[15:imgScan.shape[0]-25,15:imgScan.shape[1]-25]
    imgCropped=cv2.resize(imgCropped,(imgW,imgH))

    return imgCropped

def ThresholdedImg(img):
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgAThres=cv2.adaptiveThreshold(imgGray,255,1,1,7,2)
    imgAThres=cv2.bitwise_not(imgAThres)
    imgAThres=cv2.medianBlur(imgAThres,3)

    return imgAThres

while True:
    ret,frame=capture.read()
    frame2=frame.copy()

    # framThres=ThresholdedImg(frame)
    myFrame=basic(frame)
    scanArea=getContours(myFrame)

    if scanArea.size!=0:
        imgOutput=warp(frame,scanArea)

        cv2.imshow('Scanning Paper',imgOutput)
        # cv2.imshow('Scanned Paper 2',framThres)
        cv2.imshow('Scanning Paper Outline',frame2)

    else:

        cv2.imshow('Scanning Paper',frame)
        # cv2.imshow('Scanned Paper 2',framThres)
        cv2.imshow('Scanning Paper Outline',frame)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

    if cv2.waitKey(50) & 0xFF==ord('p'):

        cv2.imwrite("Images/ScannedImage"+str(count)+".jpg",imgOutput)
        cv2.putText(imgOutput,'Scanned Image',(50,75),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),4)
        cv2.imshow('Scanned Image',imgOutput)
        cv2.waitKey(200)
        count+=1


capture.release()
cv2.destroyAllWindows()