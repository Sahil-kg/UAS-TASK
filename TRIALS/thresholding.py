import cv2
import numpy as np 
img=cv2.imread("C:\coding programms\Desktop\coding\python\opencv2\img5.jpeg")# 0 represents gray image
imgR=cv2.resize(img,(623,600))
imgG=cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
imgB=cv2.GaussianBlur(imgG,(25,25),0)
_ , tresh = cv2.threshold(imgB,160,255,cv2.THRESH_TRUNC)
contours, hierarchy = cv2.findContours(tresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
final2=cv2.drawContours(imgB, contours, -1, (0, 255, 0), 3)
# th2 = cv2.adaptiveThreshold(imgB,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

# tresh = cv2.bitwise_not(tresh)
cv2.imshow("gray",imgB)
cv2.imshow("tresh",tresh)
# cv2.imshow("th2",th2)
# cv2.imshow("th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()