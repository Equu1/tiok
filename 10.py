import numpy as np
import cv2

def zad1():
    size = (300, 300)

    triangle1 = np.zeros(size, dtype="uint8")
    pts1 = np.array([[0, 250], [150, 0], [300, 250]])
    cv2.fillPoly(triangle1, [pts1], 255)

    circle = np.zeros(size, dtype="uint8")
    cv2.circle(circle, (150, 150), 150, 255, -1)

    bitwise_and = cv2.bitwise_and(triangle1, circle)
    bitwise_or = cv2.bitwise_or(triangle1, circle)
    bitwise_xor = cv2.bitwise_xor(triangle1, circle)
    bitwise_not_t = cv2.bitwise_not(triangle1)
    bitwise_not_c = cv2.bitwise_not(circle)

    cv2.imshow("Triangle 1", triangle1)
    cv2.imshow("Circle", circle)
    cv2.imshow("AND", bitwise_and)
    cv2.imshow("OR", bitwise_or)
    cv2.imshow("XOR", bitwise_xor)
    cv2.imshow("NOT Triangle", bitwise_not_t)
    cv2.imshow("NOT Circle", bitwise_not_c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    triangle2 = np.zeros(size, dtype="uint8")
    pts2 = np.array([[30, 250], [180, 0], [330, 250]])
    cv2.fillPoly(triangle2, [pts2], 255)

    bitwise_and2 = cv2.bitwise_and(triangle2, circle)
    bitwise_or2 = cv2.bitwise_or(triangle2, circle)
    bitwise_xor2 = cv2.bitwise_xor(triangle2, circle)
    bitwise_not_t2 = cv2.bitwise_not(triangle2)

    cv2.imshow("Triangle 2", triangle2)
    cv2.imshow("Circle", circle)
    cv2.imshow("AND (pos2)", bitwise_and2)
    cv2.imshow("OR (pos2)", bitwise_or2)
    cv2.imshow("XOR (pos2)", bitwise_xor2)
    cv2.imshow("NOT Triangle (pos2)", bitwise_not_t2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad2():
        img1 = cv2.imread("10.jpg")
        img2 = cv2.imread("10.1.jpg")

        diff = cv2.bitwise_xor(img1, img2)

        cv2.imshow("Image 1", img1)
        cv2.imshow("Image 2", img2)
        cv2.imshow("XOR Differences", diff)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    zad1()
    zad2()


if __name__ == "__main__":
    main()