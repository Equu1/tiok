import cv2
import imutils

img = cv2.imread("5image.jpg")
rotated = imutils.rotate(img, 75)

cv2.imwrite("rotated_output.jpg", rotated)
