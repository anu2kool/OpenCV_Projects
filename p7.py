import cv2
img=cv2.imread('lena.jpg')
cv2.imshow('output',img)
cv2.waitKey(0)
print(img.shape[:2])

height, width=img.shape[:2]
start_row, end_row=int(0.25*height), int(0.85*width)
start_col, end_col=int(0.25*width), int(0.95*width)

new_img=img[start_row:end_row, start_col:end_col]
cv2.imshow('outputcropped', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()