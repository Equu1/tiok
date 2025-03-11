import cv2

image = cv2.imread("image.jpg")
(h, w) = image.shape[:2]
x, y = h // 3, w // 3
center = image[x:2*x, y:2*y]
cv2.imshow("Wynik", center)
cv2.waitKey(0)
cv2.destroyAllWindows()