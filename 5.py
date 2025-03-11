import cv2

image = cv2.imread("image.jpg")
(h, w) = image.shape[:2]
cY, cX = h // 2, w // 2
image[0:cY, 0:cX] = (255, 0, 0)
cv2.imshow("Wynik", image)
cv2.waitKey(0)
cv2.destroyAllWindows()