import cv2

img = cv2.imread("5image.jpg")
M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("rotated", rotated)
cv2.waitKey(0)