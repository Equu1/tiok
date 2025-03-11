import cv2

image = cv2.imread("image.jpg")
(b1, g1, r1) = image[50, 50]
b1 = int(b1)
g1 = int(g1)
r1 = int(r1)
print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r1, g1, b1))
(b2, g2, r2) = image[200, 200]
b2 = int(b2)
g2 = int(g2)
r2 = int(r2)
print("Pixel at (200, 200) - Red: {}, Green: {}, Blue: {}".format(r2, g2, b2))
print(f"Różnica: R: {r1 - r2}, G: {g1 - g2}, B: {b1 - b2}")