import cv2

image = cv2.imread("image.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
print(f"Zadanie 11: Najjaśniejszy piksel: {max_loc}, wartość: {max_val}")