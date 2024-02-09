import numpy as np 
import cv2

img=cv2.imread("C:\coding programms\Desktop\coding\python\opencv2\img2.jpeg")
imgR=cv2.resize(img,(623,600))
imgG=cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
imgB=cv2.GaussianBlur(imgG,(25,25),0)

laplacian = cv2.Laplacian(imgB,cv2.CV_64F)
pfinal=np.absolute(laplacian)
final=np.uint(pfinal)

cv2.imshow("output",pfinal)
cv2.waitKey(0)
cv2.destroyAllWindows()