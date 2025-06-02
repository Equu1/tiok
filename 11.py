import numpy as np
import cv2

img1 = cv2.imread('11.jpg')
img2 = cv2.imread('11.1.jpg')


def zad1():

    x1, y1 = 230, 50
    x2, y2 = 305, 150

    mask = np.zeros(img1.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (x1, y1), (x2, y2), 255, -1)

    masked = cv2.bitwise_and(img1, img1, mask=mask)

    cv2.imshow("Original", img1)
    cv2.imshow("Face Mask", mask)
    cv2.imshow("Masked Face", masked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad2():
    mask = np.ones(img1.shape[:2], dtype="uint8") * 255

    cv2.rectangle(mask, (240, 80), (260, 90), 0, -1)
    cv2.rectangle(mask, (280, 80), (300, 90), 0, -1)

    masked = cv2.bitwise_and(img1, img1, mask=mask)

    cv2.imshow("Original", img1)
    cv2.imshow("Eye Cover Mask", mask)
    cv2.imshow("Hidden Eyes", masked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad3():

    hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 40, 40])
    upper_green = np.array([90, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    darkened = cv2.convertScaleAbs(img2, alpha=0.25, beta=0)

    masked_green = cv2.bitwise_and(img2, img2, mask=mask)
    masked_dark = cv2.bitwise_and(darkened, darkened, mask=cv2.bitwise_not(mask))
    result = cv2.add(masked_green, masked_dark)

    cv2.imshow("Original", img2)
    cv2.imshow("Green Color Mask", mask)
    cv2.imshow("Extracted Green Colors", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    zad1()
    zad2()
    zad3()

if __name__ == "__main__":
    main()