import cv2
import numpy as np


img = cv2.imread('C:\coding programms\Desktop\coding\python\opencv2\img.jpeg')
# imgR=cv2.resize(img,(623,600))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray) 

harris = cv2.cornerHarris(gray,2,3,0.04)  

img[harris>0.01*harris.max()]=[0,255,0]    

cv2.imshow('Harris Corners',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

