import cv2
import numpy as np

def zad1():
    img = cv2.imread('12.jpg')
    (B, G, R) = cv2.split(img)

    cv2.imshow('B', B)
    cv2.imshow('G', G)
    cv2.imshow('R', R)

    cv2.imwrite('blue_channel.jpg', B)
    cv2.imwrite('green_channel.jpg', G)
    cv2.imwrite('red_channel.jpg', R)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad2():
    img = cv2.imread('12.2.jpg')
    (B, G, R) = cv2.split(img)

    cv2.imshow('B', B)
    cv2.imshow('G', G)
    cv2.imshow('R', R)
    # Niebieskie obiekty są najjaśniejsze w kanale B

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad3():
    img = cv2.imread('12.2.jpg')
    (B, G, R) = cv2.split(img)

    #a
    swapped = cv2.merge([R, B, G])
    cv2.imshow('Swapped Channels', swapped)

    #b
    B_0 = B.copy()
    B_0[:] = 0
    merged = cv2.merge([B_0, G, R])
    cv2.imshow('Merged Channels', merged)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad4():
    img = cv2.imread('12.2.jpg')
    (B, G, R) = cv2.split(img)

    R_boosted = cv2.add(R, 50)

    new_img = cv2.merge([B, G, R_boosted])
    cv2.imshow('Original Image', img)
    cv2.imshow('Boosted Red Channel', new_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad5():
    img = cv2.imread('12.3.jpg')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    B, G, R = cv2.split(img)

    R_boosted = R.copy()

    R_boosted[mask > 0] = np.clip(R_boosted[mask > 0].astype(int) + 100, 0, 255).astype(np.uint8)

    result = cv2.merge([B, G, R_boosted])

    cv2.imshow('Original', img)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def zad6():
    img = cv2.imread('12.1.png')

    #a
    (B, G, R) = cv2.split(img)

    #b
    swapped_img = cv2.merge([R, G, B])
    cv2.imshow('Swapped Image', swapped_img)

    #c
    B_0 = np.zeros_like(B)
    no_blue = cv2.merge([B_0, G, R])

    cv2.imshow('No Blue Channel', no_blue)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    zad6()

if __name__ == "__main__":
    main()