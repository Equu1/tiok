import cv2

image = cv2.imread("image.jpg")
(h, w) = image.shape[:2]
x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
if 0 <= x < w and 0 <= y < h:
    image[y, x] = (0, 0, 0)
    cv2.imshow("Wynik", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nieprawidłowe współrzędne!")