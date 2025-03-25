import cv2
import numpy as np

img = cv2.imread("4image.jpg")
#a
tx = int(input("Podaj przesunięcie w poziomie (tx): "))
ty = int(input("Podaj przesunięcie w pionie (ty): "))
M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
#b
cv2.imshow("5b", shifted)
cv2.waitKey(0)