#Rotation matrix
import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('output', img)
cv2.waitKey(0)
height, width=img.shape[:2]
rotation_matrix=cv2.getRotationMatrix2D((width/2, height/2), 45, 0.5 )

rotation_img=cv2.warpAffine(img, rotation_matrix, (width, height))
cv2.imshow('output', rotation_img)
cv2.waitKey(0)

cv2.destroyAllWindows()