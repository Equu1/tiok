import cv2
import numpy as np
import imutils

img = cv2.imread("4image.jpg")
#a
shifted_imutils = imutils.translate(img, 100, 50)
cv2.imshow("4a", shifted_imutils)
#b
M = np.float32([[1, 0, 100], [0, 1, 50]])
shifted_warp = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("4b", shifted_warp)
cv2.waitKey(0)