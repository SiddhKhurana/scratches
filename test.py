import cv2

img = cv2.imread('C:\\Users\\sony\\Pictures\\download.jpg',cv2.IMREAD_COLOR)

cv2.imshow('Screenshot',img)
cv2.waitKey(0)
cv2.destroyAllWindows()