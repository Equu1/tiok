import cv2
import numpy as np

#a
img = cv2.imread("4image.jpg")
h, w = img.shape[:2]
tx, ty = w//2 + 50, h//2 + 50
M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(img, M, (w, h))
#b
cv2.imshow("3b", shifted)
cv2.waitKey(0)