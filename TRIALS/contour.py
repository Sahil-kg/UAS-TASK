import cv2
import numpy as np 
img=cv2.imread("C:\coding programms\Desktop\coding\python\opencv2\img2.jpeg")
imgR=cv2.resize(img,(623,600))
imgG=cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
imgB=cv2.GaussianBlur(imgG,(25,25),0)

contours, hierarchy = cv2.findContours(imgB, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(contours))
imgc=imgR.copy()
final2=cv2.drawContours(imgc, contours, -1, (0, 255, 0), 3)

cv2.imshow("output",final2)
cv2.waitKey(0)
cv2.destroyAllWindows()