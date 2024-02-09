import cv2 
import numpy as np 
p=[]
img=cv2.imread("C:\coding programms\Desktop\coding\python\INPUT IMAGES\img3.jpeg")
imgR=cv2.resize(img,(623,600))
imgG=cv2.cvtColor(imgR,cv2.COLOR_BGR2GRAY)
imgB=cv2.GaussianBlur(imgG,(25,25),0)
imgF=cv2.bilateralFilter(imgR,15,75,75)

_, tresh = cv2.threshold(imgF, 100, 255, cv2.THRESH_TRUNC)
treshG = cv2.cvtColor(tresh, cv2.COLOR_BGR2GRAY)
_, final1 = cv2.threshold(treshG, 90, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(final1, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# print(len(contours))
imgc1=imgF.copy()
final2=cv2.drawContours(imgc1, contours, -1, (0, 255, 0), 3)
for i in range (len(contours)):
    area = cv2.contourArea(contours[i])
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    p.append(len(contours))
print(len(contours))
if len(contours)!=1:
    print(len(contours))
    for i in range (len(contours)):
        area = cv2.contourArea(p)
        if (area / (img.shape[0] * img.shape[1]) > 0.9 ):
            _ , tresh2 = cv2.threshold(imgB,100,255,cv2.THRESH_BINARY_INV)
            contours, _ = cv2.findContours(tresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
elif len(contours)==1:
        area = cv2.contourArea(contours[0])
        if (area / (img.shape[0] * img.shape[1]) > 0.9 ):
            _ , tresh2 = cv2.threshold(imgB,100,255,cv2.THRESH_BINARY_INV)
            contours, _ = cv2.findContours(tresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            contours = sorted(contours, key=cv2.contourArea, reverse=True)

contour_img=np.zeros_like(imgG)
cv2.drawContours(contour_img, contours, 0, (255,255,255), -1)

final2=cv2.bitwise_and(imgR,imgR,mask=contour_img)

# cv2.imshow("output2",imgc)
cv2.imshow("output",final2)
cv2.waitKey(0)
cv2.destroyAllWindows()