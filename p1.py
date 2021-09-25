import cv2
img=cv2.imread('lena.jpg')
cv2.imshow('Output1', img)
cv2.waitKey(0)
gray_img=cv2.imread('lena.jpg',0)
cv2.imshow('output3', gray_img)
cv2.waitKey(0)

ret, bw=cv2.threshold(gray_img, 57, 255, cv2.THRESH_TRIANGLE)
cv2.imshow('triangle', bw)
cv2.waitKey(0)

ret, bw=cv2.threshold(gray_img, 57, 255, cv2.THRESH_OTSU)
cv2.imshow('otsu', bw)
cv2.waitKey(0)

ret, bw=cv2.threshold(gray_img, 57, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', bw)
cv2.waitKey(0)

ret, bw=cv2.threshold(gray_img, 57, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('inv', bw)
cv2.waitKey(0)

cv2.destroyAllWindows()