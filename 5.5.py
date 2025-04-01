import cv2
import imutils

img = cv2.imread("5image.jpg")
rotated = imutils.rotate(img, 180)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)