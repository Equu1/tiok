import cv2
import imutils

img = cv2.imread("5image.jpg")

for angle in range(0, 360, 15):
    rotated = imutils.rotate(img, angle)
    cv2.imshow("obracanie", rotated)
    cv2.waitKey(500)