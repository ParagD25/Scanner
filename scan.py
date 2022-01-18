import cv2

capture=cv2.VideoCapture(0)

def basic(frame):

    frameG=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameBlur=cv2.GaussianBlur(frameG,(7,7),1)
    frameCanny=cv2.Canny(frameBlur,150,150)

    return frameCanny



while True:
    ret,frame=capture.read()

    myFrame=basic(frame)

    cv2.imshow('Result',myFrame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()