import cv2

img = cv2.imread("5image.jpg")
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))

cv2.imshow("rotated", rotated)
cv2.waitKey(0)