import cv2
import numpy as np 
img=cv2.imread("C:\coding programms\Desktop\coding\python\INPUT IMAGES\img7.jpeg")# 0 represents gray image
imgR=cv2.resize(img,(623,600))
imgG=cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
imgB=cv2.GaussianBlur(imgG,(25,25),0)
imgF=cv2.bilateralFilter(imgR,15,75,75)
dst = cv2.fastNlMeansDenoisingColored(imgF,None,10,10,7,21)


_ , tresh = cv2.threshold(dst,100,255,cv2.THRESH_TRUNC)
treshG = cv2.cvtColor(tresh, cv2.COLOR_BGR2GRAY)
_, final1 = cv2.threshold(treshG, 90, 255, cv2.THRESH_BINARY)


tresh2 = cv2.bitwise_not(final1)
cv2.imshow("gray",tresh2)
# cv2.imshow("tresh",final1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# dst = cv2.fastNlMeansDenoisingColored(imgB,None,10,10,7,21)