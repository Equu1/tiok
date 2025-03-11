import cv2

image = cv2.imread("image.jpg")
(h, w) = image.shape[:2]
cv2.imshow("Przed", image)
image[50:101, 50:101] = (255, 255, 255)
cv2.imshow("Po", image)
cv2.waitKey(0)
cv2.destroyAllWindows()