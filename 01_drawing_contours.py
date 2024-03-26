import cv2
import numpy as np

img = cv2.imread("05_Contours/resimd/contour1.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


_, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
##print(thresh)
## output : [[255 255 255 ... 255 255 255]
## [255 255 255 ... 255 255 255]
## [255 255 255 ... 255 255 255]
## ...
## [255 255 255 ... 255 255 255]
## [255 255 255 ... 255 255 255]
## [255 255 255 ... 255 255 255]]
contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img,contours, -1, (0,0,255), 3)

cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows
