import cv2

img = cv2.imread("5image.jpg")
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotated = img.copy()
for i in range(3):
    M = cv2.getRotationMatrix2D((cX, cY), 30, 1.0)
    rotated = cv2.warpAffine(rotated, M, (w, h))


M = cv2.getRotationMatrix2D((cX, cY), 90, 1.0)
rotated_90 = cv2.warpAffine(img, M, (w, h))

cv2.imshow("3x30", rotated)
cv2.imshow("90", rotated_90)
cv2.waitKey(0)