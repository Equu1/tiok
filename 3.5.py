import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
for size in range(0, 175, 20):
    half = size // 2
    cv2.rectangle(canvas,(centerX - half, centerY - half),(centerX + half, centerY + half),(255, 255, 255), 1)
cv2.imshow("5", canvas)
cv2.waitKey(0)