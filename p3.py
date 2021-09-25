#Translation of the image in different quadrants
import cv2
import numpy as np
img=cv2.imread('lena.jpg')
cv2.imshow('output', img)
cv2.waitKey(0)

height, width=img.shape[:2] #gives size as a tuple (height, width)
print(height)
print(width)

new_height, new_width= -height/2, width/2
T=np.float32([[1, 0, new_width], #translation matrix of 2x3 sie to convert image
              [0, 1, new_height]])
print(T)

#warpAffine for linear transformation
translation_img=cv2.warpAffine(img, T, (width, height))
cv2.imshow('output', translation_img)
cv2.waitKey(0)
#size of the image remains the same but it justs shift acc. to the coordinates specified
print(translation_img.shape[:2])
cv2.destroyAllWindows()