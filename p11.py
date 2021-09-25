#edge detection
import numpy as np
import cv2

img=cv2.imread('lena.jpg',0)
cv2.imshow('output1', img)
cv2.waitKey(0)

height, width=img.shape
sobel_x=cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y=cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('sobelx', sobel_x)
cv2.waitKey(0)

cv2.imshow('sobely', sobel_y)
cv2.waitKey(0)

sobelor=cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('sobel or', sobelor)
cv2.waitKey(0)

laplacian=cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('Laplacian', laplacian)
cv2.waitKey(0)

canny=cv2.Canny(img, 40, 120)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
