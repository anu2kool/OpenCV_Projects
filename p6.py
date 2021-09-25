import cv2

img=cv2.imread('lena.jpg')
cv2.imshow('output', img)
cv2.waitKey(0)

#Linear Interpolation most clear resizing
new_img=cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imshow('1output', new_img)
cv2.waitKey(0)

#Area Interpolation less clear compared to linear
new_img=cv2.resize(img, (440,440), interpolation=cv2.INTER_AREA)
cv2.imshow('2output', new_img)
cv2.waitKey(0)

#Cubic interpolation less clear compared to linear
new_img=cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('3output', new_img)
cv2.waitKey(0)

#Resizing image to double and half of its initial size using pyramid
new_img=cv2.pyrUp(img)
cv2.imshow('4output', new_img)
cv2.waitKey(0)

new_img=cv2.pyrDown(img)
cv2.imshow('5output', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
