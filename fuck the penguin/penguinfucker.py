import cv2.cv2 as cv2
import numpy as np
from numpy.matrixlib.defmatrix import matrix

def empty(a):
    pass

path='Resources/zy.jpg'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",800,300)

cv2.createTrackbar("Hue Min",'TrackBars',56,255,empty)
cv2.createTrackbar("Hue Max",'TrackBars',171,255,empty)
cv2.createTrackbar("Sat Min",'TrackBars',27,255,empty)
cv2.createTrackbar("Sat Max",'TrackBars',237,255,empty)
cv2.createTrackbar("Val Min",'TrackBars',201,255,empty)
cv2.createTrackbar("Val Max",'TrackBars',255,255,empty)


while True:
    img=cv2.imread(path)
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min",'TrackBars')
    h_max = cv2.getTrackbarPos("Hue Max",'TrackBars')
    s_min = cv2.getTrackbarPos("Sat Min",'TrackBars')
    s_max = cv2.getTrackbarPos("Sat Max",'TrackBars')
    v_min = cv2.getTrackbarPos("Val Min",'TrackBars')
    v_max = cv2.getTrackbarPos("Val Max",'TrackBars')
    #print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper) #create a mask
    imgResult=cv2.bitwise_and(img,img,mask=mask)


    cv2.imshow("Image",img)
    #cv2.imshow("HSV",imgHSV)
    #cv2.imshow("mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)
