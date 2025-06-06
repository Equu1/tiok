import cv2
import numpy as np
import matplotlib.pyplot as plt


def zad1():
    #a
    img = cv2.imread("13.jpg")

    #b
    kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))

    eroded_rect = cv2.erode(img, kernel_rect)
    eroded_ellipse = cv2.erode(img, kernel_ellipse)

    cv2.imshow("Original Image", img)
    cv2.imshow("Eroded with Rectangular Kernel", eroded_rect)
    cv2.imshow("Eroded with Elliptical Kernel", eroded_ellipse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #c
    #Erozja powoduje:
    # - Zmniejszenie obszaru jasnych elementów na obrazie
    # - Element eliptyczny daje bardziej gładkie krawędzie
    # - Element prostokątny daje bardziej kanciaste krawędzie

def zad2():
    img = cv2.imread("13.jpg")

    iterations = [1, 3, 5]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    results = []

    for i in iterations:
        dilated = cv2.dilate(img, kernel, iterations=i)
        results.append(dilated)

    plt.figure(figsize=(15, 5))

    plt.subplot(141), plt.imshow(img, cmap='gray'), plt.title('Oryginał')
    for idx, i in enumerate(iterations):
        plt.subplot(142 + idx)
        plt.imshow(results[idx], cmap='gray')
        plt.title(f'Dylatacja x{i}')

    plt.tight_layout()
    plt.show()

def zad3():
    img = cv2.imread("13.1.png", cv2.IMREAD_GRAYSCALE)

    kernel_sizes = [(3, 3), (5, 5), (7, 7)]

    plt.figure(figsize=(15, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Oryginał')
    plt.axis('off')

    for i, size in enumerate(kernel_sizes):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, size)
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        plt.subplot(2, 2, i + 2)
        plt.imshow(opening, cmap='gray')
        plt.title(f'Otwarcie {size[0]}×{size[1]}')
        plt.axis('off')

    plt.tight_layout()
    plt.show()

    # Ocena skuteczności usuwania szumu
    # Operacja otwarcia skutecznie usuwa biały szum ('sól'),
    # ale jednocześnie powiększa i uwydatnia czarny szum ('pieprz').
    # Efekt ten wzrasta wraz z rozmiarem elementu strukturalnego.


def zad4():
    img = cv2.imread("13.2.png")

    kernel_shapes = [
        ("Prostokąt", cv2.MORPH_RECT),
        ("Elipsa", cv2.MORPH_ELLIPSE),
        ("Krzyż", cv2.MORPH_CROSS)
    ]

    kernel_size = (13, 13)

    plt.figure(figsize=(15, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Oryginał')
    plt.axis('off')

    for i, (shape_name, shape_type) in enumerate(kernel_shapes):
        kernel = cv2.getStructuringElement(shape_type, kernel_size)
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

        plt.subplot(2, 2, i + 2)
        plt.imshow(closing, cmap='gray')
        plt.title(f'Zamknięcie: {shape_name}')
        plt.axis('off')

    plt.tight_layout()
    plt.show()


def zad5():
    img = cv2.imread("13.1.png", cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Nie znaleziono obrazu.")
        return

    kernel_shapes = {
        "Prostokąt": cv2.MORPH_RECT,
        "Elipsa": cv2.MORPH_ELLIPSE,
        "Krzyż": cv2.MORPH_CROSS
    }

    operations = {
        "Erozja": cv2.MORPH_ERODE,
        "Dylatacja": cv2.MORPH_DILATE,
        "Otwarcie": cv2.MORPH_OPEN,
        "Zamknięcie": cv2.MORPH_CLOSE,
        "Gradient": cv2.MORPH_GRADIENT
    }

    kernel_size = (5, 5)
    fig, axs = plt.subplots(len(operations), len(kernel_shapes) + 1, figsize=(15, 10))
    fig.suptitle("Operacje morfologiczne dla różnych elementów strukturalnych", fontsize=16)

    for row_idx, (op_name, op_code) in enumerate(operations.items()):
        axs[row_idx, 0].imshow(img, cmap='gray')
        axs[row_idx, 0].set_title("Oryginał")
        axs[row_idx, 0].axis('off')

        for col_idx, (shape_name, shape_type) in enumerate(kernel_shapes.items()):
            kernel = cv2.getStructuringElement(shape_type, kernel_size)
            result = cv2.morphologyEx(img, op_code, kernel)

            axs[row_idx, col_idx + 1].imshow(result, cmap='gray')
            axs[row_idx, col_idx + 1].set_title(f"{op_name}\n{shape_name}")
            axs[row_idx, col_idx + 1].axis('off')

    plt.tight_layout()
    plt.show()

'''
Elementy strukturalne mają różne kształty i wpływają na wyniki operacji morfologicznych:

Prostokątne: 
tworzą ostrzejsze, kanciaste efekty – skuteczniejsze do usuwania prostokątnych artefaktów.

Eliptyczne: 
dają łagodniejsze, bardziej naturalne kontury – dobre przy obrazach z okrągłymi kształtami (np. komórki).

Krzyżowe: 
przetwarzają piksele tylko w 4 kierunkach – mogą pozostawiać więcej szczegółów i dziur, ale są bardziej selektywne.
'''

def zad6():
    img = cv2.imread("13.3.jpg", cv2.IMREAD_GRAYSCALE)

    kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_open)

    kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel_close)

    kernel_grad = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    gradient = cv2.morphologyEx(closed, cv2.MORPH_GRADIENT, kernel_grad)

    titles = ['Oryginał', 'Po otwarciu (usuwa szum)', 'Po zamknięciu (łączy znaki)', 'Gradient (kontury)']
    images = [img, opened, closed, gradient]

    plt.figure(figsize=(12, 6))
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()


def main():
    zad6()

if __name__ == "__main__":
    main()