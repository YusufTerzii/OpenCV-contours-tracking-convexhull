import cv2
import numpy as np

cap = cv2.VideoCapture("05_Contours/resimd/dog.mp4")

while True:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(860,480))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    sensitivity=15
    lower_white = np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])

    mask = cv2.inRange(hsv,lower_white,upper_white)
    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()





