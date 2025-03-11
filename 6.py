import cv2

image = cv2.imread("image.jpg")
(h, w) = image.shape[:2]
cY, cX = h // 2, w // 2
image[cY-50:cY+50, cX-50:cX+50] = (0, 0, 255)
cv2.imshow("Wynik", image)
cv2.waitKey(0)
cv2.destroyAllWindows()