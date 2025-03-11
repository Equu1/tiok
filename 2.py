import cv2

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]

(b, g, r) = image[h-1, w-1]
print("Original - Red: {}, Green: {}, Blue: {}".format(r, g, b))
cv2.imshow("Original", image)
image[h-1, w-1] = (0, 0, 255)
(b, g, r) = image[h-1, w-1]
print("Changed - Red: {}, Green: {}, Blue: {}".format(r, g, b))
cv2.imshow("Changed", image)
cv2.waitKey(0)
cv2.destroyAllWindows()