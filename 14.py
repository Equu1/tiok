import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_images(title, images):
    cols = 4
    rows = (len(images) + cols - 1) // cols
    plt.figure(figsize=(4 * cols, 4 * rows))
    for i, (label, img) in enumerate(images):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.subplot(rows, cols, i + 1)
        plt.imshow(img_rgb)
        plt.title(label)
        plt.axis("off")
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

def zad1():
    image = cv2.imread("14.jpg")
    kernel_sizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

    avg_results = [(f"Average Blur ({kX}x{kY})", cv2.blur(image, (kX, kY))) for (kX, kY) in kernel_sizes]
    gauss_results = [(f"Gaussian Blur ({kX}x{kY})", cv2.GaussianBlur(image, (kX, kY), 0)) for (kX, kY) in kernel_sizes]
    median_results = [(f"Median Blur ({k})", cv2.medianBlur(image, k)) for k in [3, 5, 9, 15]]
    bilateral_results = [(f"Bilateral (d={d}, sc={sc}, ss={ss})", cv2.bilateralFilter(image, d, sc, ss)) for (d, sc, ss) in [(11, 21, 7), (11, 41, 21), (11, 61, 39)]]

    show_images("Average Blur", [("Original", image)] + avg_results)
    show_images("Gaussian Blur", [("Original", image)] + gauss_results)
    show_images("Median Blur", [("Original", image)] + median_results)
    show_images("Bilateral Blur", [("Original", image)] + bilateral_results)

    # i. Median blur najlepiej usuwa szum
    # ii. Bilateral najlepiej zachowuje szczegóły
    # iii.
    # - blur: szybki, ale traci krawędzie i detale
    # - gaussian: lepszy niż blur, zachowuje trochę więcej szczegółów
    # - median: świetny przy szumie, może zniekształcać detale
    # - bilateral: najwolniejszy, ale zachowuje krawędzie i dobrze filtruje szum


def zad2():
    image = cv2.imread("14.4.jpg")

    kernel_sizes = [(3, 3), (5, 5), (9, 9), (15, 15)]

    avg_results = [(f"Average Blur ({kX}x{kY})", cv2.blur(image, (kX, kY))) for (kX, kY) in kernel_sizes]
    gauss_results = [(f"Gaussian Blur ({kX}x{kY})", cv2.GaussianBlur(image, (kX, kY), 0)) for (kX, kY) in kernel_sizes]
    median_results = [(f"Median Blur ({k})", cv2.medianBlur(image, k)) for k in [3, 5, 9, 15]]

    show_images("Average Blur", [("Original", image)] + avg_results)
    show_images("Gaussian Blur", [("Original", image)] + gauss_results)
    show_images("Median Blur", [("Original", image)] + median_results)

    # i. Większy kernel = mocniejsze rozmycie, większa utrata szczegółów
    # ii. Optymalne wartości: 5 lub 9 - kompromis między wygładzeniem a zachowaniem detali

def zad3():
    image = cv2.imread("14.1.jpg")

    params = [11, 21, 7], [11, 41, 21], [11, 61, 39]
    kernel_sizes = [(3, 3), (5, 5), (9, 9)]

    bilateral_results = [(f"Bilateral (d={d}, sc={sc}, ss={ss})", cv2.bilateralFilter(image, d, sc, ss)) for (d, sc, ss)in params]
    avg_results = [(f"Average Blur ({kX}x{kY})", cv2.blur(image, (kX, kY))) for (kX, kY) in kernel_sizes]
    gauss_results = [(f"Gaussian Blur ({kX}x{kY})", cv2.GaussianBlur(image, (kX, kY), 0)) for (kX, kY) in kernel_sizes]
    median_results = [(f"Median Blur ({k})", cv2.medianBlur(image, k)) for k in [3, 5, 9]]

    show_images("Bilateral Blur", [("Original", image)] + bilateral_results)
    show_images("Average Blur", [("Original", image)] + avg_results)
    show_images("Gaussian Blur", [("Original", image)] + gauss_results)
    show_images("Median Blur", [("Original", image)] + median_results)

    # i. Tak, bilateral redukuje szum skutecznie
    # ii. Zachowuje lepiej szczegóły niż median, average i gaussian
    # iii. Najlepsze: (11, 41, 21)

def zad4():
    image = cv2.imread("14.2.jpg")

    params = [11, 21, 7], [11, 41, 21], [11, 61, 39]
    kernel_sizes = [(3, 3), (5, 5), (9, 9)]

    bilateral_results = [(f"Bilateral (d={d}, sc={sc}, ss={ss})", cv2.bilateralFilter(image, d, sc, ss)) for (d, sc, ss) in params]
    avg_results = [(f"Average Blur ({kX}x{kY})", cv2.blur(image, (kX, kY))) for (kX, kY) in kernel_sizes]
    gauss_results = [(f"Gaussian Blur ({kX}x{kY})", cv2.GaussianBlur(image, (kX, kY), 0)) for (kX, kY) in kernel_sizes]
    median_results = [(f"Median Blur ({k})", cv2.medianBlur(image, k)) for k in [3, 5, 9]]

    show_images("Bilateral Blur", [("Original", image)] + bilateral_results)
    show_images("Average Blur", [("Original", image)] + avg_results)
    show_images("Gaussian Blur", [("Original", image)] + gauss_results)
    show_images("Median Blur", [("Original", image)] + median_results)

    # Komentarz:
    # i. Najmocniej rozmywa tekst: blur, median
    # ii. Najlepiej zachowuje czytelność: bilateral, gaussian

def zad5():
    image = cv2.imread("14.jpg")
    noise = np.zeros_like(image)
    cv2.randn(noise, (0, 0, 0), (30, 30, 30))
    noisy = cv2.add(image, noise)

    params = [11, 21, 7], [11, 41, 21], [11, 61, 39]
    kernel_sizes = [(3, 3), (5, 5), (9, 9)]

    bilateral_results = [(f"Bilateral (d={d}, sc={sc}, ss={ss})", cv2.bilateralFilter(noisy, d, sc, ss)) for (d, sc, ss) in params]
    avg_results = [(f"Average Blur ({kX}x{kY})", cv2.blur(noisy, (kX, kY))) for (kX, kY) in kernel_sizes]
    gauss_results = [(f"Gaussian Blur ({kX}x{kY})", cv2.GaussianBlur(noisy, (kX, kY), 0)) for (kX, kY) in kernel_sizes]
    median_results = [(f"Median Blur ({k})", cv2.medianBlur(noisy, k)) for k in [3, 5, 9]]

    show_images("Bilateral Blur", [("Original", noisy)] + bilateral_results)
    show_images("Average Blur", [("Original", noisy)] + avg_results)
    show_images("Gaussian Blur", [("Original", noisy)] + gauss_results)
    show_images("Median Blur", [("Original", noisy)] + median_results)

    # Bilateral najlepiej usuwa szum, z zachowaniem szczegółów

def zad6():
    image = cv2.imread("14.3.jpg")
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (340, 180), (440, 225), 255, -1)
    blurred = cv2.GaussianBlur(image, (17, 17), 0)
    focus = np.where(mask[..., None] == 255, image, blurred)
    cv2.imshow("Depth of Field Effect", focus)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    zad6()

if __name__ == "__main__":
    main()
