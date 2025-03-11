import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Przed", image)
image[99,:] = (0, 255, 0)
cv2.imshow("Po", image)
cv2.waitKey(0)
cv2.destroyAllWindows()