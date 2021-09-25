import cv2
import numpy as np

img=cv2.imread('lena.jpg')
cv2.imshow("Output1", img)
cv2.waitKey(0)

kernel1=np.ones((3,3), np.float32)/9
blur1=cv2.filter2D(img, -1, kernel1)
cv2.imshow('Output2', blur1)
cv2.waitKey(0)

kernel2=np.ones((5,5), np.float32)/25
blur2=cv2.filter2D(img, -1, kernel2)
cv2.imshow('Output3', blur2)
cv2.waitKey(0)

kernel3=np.ones((9,9), np.float32)/81
blur3=cv2.filter2D(img, -1, kernel3)
cv2.imshow('Output3', blur3)
cv2.waitKey(0)

cv2.destroyAllWindows()