#rotating through transpose
import cv2
img=cv2.imread('lena.jpg')


T1_image=cv2.transpose(img)
T_image=cv2.transpose(cv2.transpose(cv2.transpose(cv2.transpose(T1_image))))
cv2.imshow('output', T_image)
cv2.waitKey(0)

cv2.destroyAllWindows()