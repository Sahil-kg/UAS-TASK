import cv2
import numpy as np 
img=cv2.imread("C:\coding programms\Desktop\coding\python\opencv2\img3.jpeg")
imgR=cv2.resize(img,(623,600))
imgG=cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
imgB=cv2.GaussianBlur(imgG,(25,25),0)
imgF=cv2.bilateralFilter(imgR,15,75,75,cv2.BORDER_CONSTANT)
# imgB=cv2.GaussianBlur(imgG,(7,7),0)
_ , tresh = cv2.threshold(imgG,160,255,cv2.THRESH_BINARY)
edges=cv2.Canny(tresh,0,190)
# print(len(edges))
contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(contours))
# imgC=imgG
contour_img=np.zeros_like(imgG)
cv2.drawContours(contour_img, contours, 0, (255,255,255), -1)

final=cv2.bitwise_and(imgF,imgF,mask=contour_img)
# final=cv2.drawContours(imgF,contours,0,(0,255,0),-1)
# cv2.imshow("img",imgG)
cv2.imshow("contour",edges)
cv2.imshow("output",final)
cv2.waitKey(0)
cv2.destroyAllWindows()