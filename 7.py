import cv2

img = cv2.imread("7image.jpg")

def zad1():
    flipped = cv2.flip(img, 1)
    cv2.imshow("1", flipped)
    cv2.waitKey(0)

def zad2():
    flipped = cv2.flip(img, 0)
    cv2.imshow("2", flipped)
    cv2.waitKey(0)

def zad3():
    flipped = cv2.flip(img, -1)
    cv2.imshow("3", flipped)
    cv2.waitKey(0)

def zad4():
    flipped_h = cv2.flip(img, 1)
    flipped_v = cv2.flip(img, 0)
    flipped_both = cv2.flip(img, -1)

    cv2.imshow("4i. Oryginal", img)
    cv2.imshow("4ii. Poziome", flipped_h)
    cv2.imshow("4iii. Pionowe", flipped_v)
    cv2.imshow("4iv. Obustronne", flipped_both)
    cv2.waitKey(0)

def zad5():
    h, w = img.shape[:2]

    crop = img[:, w // 2:]
    flipped_crop = cv2.flip(crop, 1)

    img[:, w // 2:] = flipped_crop
    cv2.imshow("5", img)
    cv2.waitKey(0)

def zad6():
    while True:
        choice = int(input("Wybierz sposob odbicia obrazu (0 – pionowe, 1 – poziome, -1 – oba): "))
        if choice in [1,0,-1]:
            flipped = cv2.flip(img, choice)
            cv2.imshow("6", flipped)
            cv2.waitKey(0)
            break
        print("Nieprawidlowy wybor")

def main():
    zad1()

if __name__=="__main__":
    main()