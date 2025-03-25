import numpy as np
import cv2

canvas = np.zeros((400, 400, 3), dtype="uint8")

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
end = (400,400)
blue = (255,0,0)
cv2.line(canvas, (centerX,centerY), end, blue, 2)
cv2.imshow("1", canvas)
cv2.waitKey(0)