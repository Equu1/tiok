import cv2

#ZAD1
image = cv2.imread("1.jpg")
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    cv2.imshow("Poprawny obraz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#ZAD2
image_color = cv2.imread("3.jpg")
if image_color is not None:
    channels = image_color.shape[2]
    print(f"Liczba kanałów (kolor): {channels}")

#ZAD3
image_gray = cv2.imread("1.jpg", cv2.IMREAD_GRAYSCALE)
if image_gray is not None:
    channels = 1 if len(image_gray.shape) == 2 else image_gray.shape[2]
    print(f"Liczba kanałów (szarość): {channels}")

#ZAD4
if image_gray is not None:
    cv2.imwrite("4.jpg", image_gray)

#ZAD5
img1 = cv2.imread("1.jpg")
img2 = cv2.imread("3.jpg")
if img1 is not None and img2 is not None:
    cv2.imshow("Obraz 1", img1)
    cv2.imshow("Obraz 2", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#ZAD6
image = cv2.imread("2.jpg")
if image is not None:
    cv2.namedWindow("Dostosowane okno", cv2.WINDOW_NORMAL)
    cv2.imshow("Dostosowane okno", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()