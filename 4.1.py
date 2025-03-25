import cv2
import numpy as np

#a
img = cv2.imread("4image.jpg")
cv2.imshow("1a", img)
cv2.waitKey(0)

#b
M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

#c
cv2.imshow("1c", shifted)
cv2.waitKey(0)