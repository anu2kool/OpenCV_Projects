import cv2
import numpy as np
import random 
image=cv2.imread('lena.jpg')
cv2.imshow('Output', image)
cv2.waitKey(0)

new_img=cv2.blur(image, (9,9))
cv2.imshow('O1', new_img)
cv2.waitKey(0)

new_img=cv2.GaussianBlur(image, (9,9), 0)
cv2.imshow('O2', new_img)
cv2.waitKey(0)


new_img=cv2.medianBlur(image,9)
cv2.imshow('O3', new_img)
cv2.waitKey(0)

new_img=cv2.bilateralFilter(image, 19, 19, 109)
cv2.imshow('O4', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()