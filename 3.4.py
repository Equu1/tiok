import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

cv2.rectangle(canvas, (100,100), (200,200), (255,255,255))
cv2.circle(canvas, (centerX, centerY), 30, (255,255,255))

cv2.imshow("4", canvas)
cv2.waitKey(0)