import cv2
import numpy as np 
import matplotlib.pyplot as plt
img=cv2.imread("C:\coding programms\Desktop\coding\python\opencv2\img.jpg")# 0 represents gray image
imgR=cv2.resize(img,(623,600))
imgG=cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
lower_white=np.array(255) 
upper_white=np.array(255)
mask=cv2.inRange(imgG,lower_white,upper_white)
bit=cv2.bitwise_and(imgG,imgG,mask=mask)
cv2.imshow("output",imgG)
cv2.imshow("bitwise",bit)
cv2.waitKey(0)
cv2.destroyAllWindows()