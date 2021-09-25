#image arithmetic operations
import numpy as np
import cv2
image1=cv2.imread('lena.jpg')
cv2.imshow('output', image1)
cv2.waitKey(0)


M=np.ones(image1.shape, dtype='uint8')*100
added=cv2.add(image1,M)
cv2.imshow('added', added)

M=np.ones(image1.shape, dtype='uint8')*150
subtract=cv2.subtract(image1,M)
cv2.imshow('subtract', subtract)
cv2.waitKey(0)

cv2.destroyAllWindows()