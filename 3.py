import cv2

image = cv2.imread('image.jpg')
(h, w) = image.shape[:2]
cX, cY = w // 2, h // 2
(b, g, r) = image[cY, cX]
print(f"Zadanie 3: Środek obrazu ({cX}, {cY}) - R: {r}, G: {g}, B: {b}")