#Extracting the different shades and their combinations

import cv2
import numpy as np
img=cv2.imread('lena.jpg')
cv2.imshow('output',img)
cv2.waitKey(0)

b,g,r=cv2.split(img)
zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Red", cv2.merge([zeroes, zeroes, r]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Green", cv2.merge([zeroes, g, zeroes]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Blue", cv2.merge([b, zeroes, zeroes]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Red Blue", cv2.merge([b, zeroes, r]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Red Green", cv2.merge([zeroes, g, r]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Green Blue", cv2.merge([b, g, zeroes]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Red Red", cv2.merge([zeroes, r, r]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Red Red", cv2.merge([r, zeroes, r]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Blue Blue", cv2.merge([zeroes, b, b]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Blue Blue", cv2.merge([b, zeroes, b]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Blue Blue", cv2.merge([b, b, zeroes]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Blue Blue", cv2.merge([b, b, b]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Green", cv2.merge([zeroes, g, g]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("G2", cv2.merge([g,g, zeroes]))
cv2.waitKey(0)

zeroes=np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("alpha", cv2.merge([b, r, g]))
cv2.waitKey(0)
print(r, g, b)

cv2.destroyAllWindows()