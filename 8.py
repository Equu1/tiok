import cv2

img1 = cv2.imread("8image.jpg")
img2 = cv2.imread("8_1.jpg")

h, w = img1.shape[:2]

def zad1():
    roi = img1[0:100, 0:100]
    cv2.imshow("1", roi)
    cv2.waitKey(0)

def zad2():
    lower = img1[h // 2:h, 0:w]
    cv2.imshow("2", lower)
    cv2.waitKey(0)

def zad3():
    right = img1[0:h, w // 2:w]
    cv2.imshow("3", right)
    cv2.waitKey(0)

def zad4():
    startX = int(input("Podaj wartosc startX: "))
    endX = int(input("Podaj wartosc endX: "))
    startY = int(input("Podaj wartosc startY: "))
    endY = int(input("Podaj wartosc endY: "))

    sliced = img1[startY:endY, startX:endX]

    cv2.imshow("4", sliced)
    cv2.waitKey(0)

def zad5():
    sliced = img2[30:160,220:310]
    cv2.imshow("5", sliced)
    cv2.waitKey(0)

def zad6():
    sliced = img1[0:h, w//2:w]
    img1[0:h, 0:w//2] = sliced
    cv2.imshow("6", img1)
    cv2.waitKey(0)

def zad7():
    rows = 3
    cols = 3
    for i in range(rows):
        for j in range(cols):
            y_start = i * (h // rows)
            y_end = (i + 1) * (h // rows)
            x_start = j * (w // cols)
            x_end = (j + 1) * (w // cols)
            tile = img1[y_start:y_end, x_start:x_end]
            cv2.imshow(f"Kafelek {i + 1}x{j + 1}", tile)
    cv2.waitKey(0)

def zad8():
    x = 0
    while x + 250 <= w:
        roi = img1[0:h, x:x + 250]
        cv2.imshow("8", roi)
        cv2.waitKey(10)
        x += 1

def zad9():
    roi = img1[h//2:h//2+300,w//2:w//2+300]
    cv2.imwrite("cropped_image.jpg", roi)

def main():
    zad1()

if __name__ == "__main__":
    main()