import cv2
import numpy as np

img = cv2.imread("9.jpg")

def zad1():
    M = np.ones_like(img) * 50
    added = cv2.add(img, M)

    added_np = img.astype(int) + 50
    added_np = np.clip(added_np, 0, 255).astype(np.uint8)

    cv2.imshow("Lighter_cv2", added)
    cv2.imshow("Lighter_np", added_np)
    cv2.waitKey(0)

def zad2():
    M = np.ones_like(img) * 150
    added = cv2.add(img, M)

    added_np = img.astype(int) + 150
    added_np = np.clip(added_np, 0, 255).astype(np.uint8)
    cv2.imshow("2_cv2", added)
    cv2.imshow("2_np", added_np)
    cv2.waitKey(0)

def zad3():
    M = np.ones_like(img) * 80
    subtracted = cv2.subtract(img, M)

    subtracted_np = img.astype(int) - 80
    subtracted_np = np.clip(subtracted_np, 0, 255).astype(np.uint8)
    cv2.imshow("2_cv2", subtracted)
    cv2.imshow("2_np", subtracted_np)
    cv2.waitKey(0)

def zad4():
    B, G, R = cv2.split(img)

    R_filtered = cv2.add(R, 30)
    G_filtered = cv2.subtract(G, 20)
    B_filtered = cv2.add(B, 10)

    filtered_image = cv2.merge([B_filtered, G_filtered, R_filtered])

    cv2.imshow('Original', img)
    cv2.imshow('Instagram Filter', filtered_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad5():
    img2 = cv2.imread("9.1.jpg")

    diff = cv2.absdiff(img, img2)

    cv2.imshow('Image 1', img)
    cv2.imshow('Image 2', img2)
    cv2.imshow('Difference', diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    zad5()

if __name__ == "__main__":
    main()