import cv2
cap=cv2.VideoCapture(0)

while True:
    ret, img=cap.read()
    laplacian=cv2.Laplacian(img, cv2.CV_64F)
    cv2.imshow('Laplacian', laplacian)
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()

