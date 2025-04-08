import cv2
import imutils

img = cv2.imread("6image.jpg")
h, w = img.shape[:2]

def zad1():
    resized = cv2.resize(img, (w//2, h//2), interpolation=cv2.INTER_AREA)
    cv2.imshow("1",resized)
    cv2.waitKey(0)

def zad2():
    resized = cv2.resize(img, (w*2, h*2), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("2", resized)
    cv2.waitKey(0)

def zad3():
    resized = cv2.resize(img, (200, 300))
    cv2.imshow("3", resized)
    cv2.waitKey(0)

def zad4():
    resized_nearest = cv2.resize(img, (w * 3, h * 3), interpolation=cv2.INTER_NEAREST)
    resized_linear = cv2.resize(img, (w * 3, h * 3), interpolation=cv2.INTER_LINEAR)
    resized_cubic = cv2.resize(img, (w * 3, h * 3), interpolation=cv2.INTER_CUBIC)
    resized_lanczos4 = cv2.resize(img, (w * 3, h * 3), interpolation=cv2.INTER_LANCZOS4)

    cv2.imshow("nearest", resized_nearest)
    cv2.imshow("linear", resized_linear)
    cv2.imshow("cubic", resized_cubic)
    cv2.imshow("lanczos4", resized_lanczos4)

    cv2.waitKey(0)

def zad5():
    resized = imutils.resize(img, width=500)
    cv2.imshow("5", resized)
    cv2.waitKey(0)

def zad6():
    resized = imutils.resize(img, height=400)
    cv2.imshow("6", resized)
    cv2.waitKey(0)

def zad7():
    resized_area = cv2.resize(img, (w//5, h//5), interpolation=cv2.INTER_AREA)
    resized_linear = cv2.resize(img, (w//5, h//5), interpolation=cv2.INTER_LINEAR)
    cv2.imshow("Area", resized_area)
    cv2.imshow("Linear", resized_linear)
    cv2.waitKey(0)

def zad8():
    resized_cubic = cv2.resize(img, (w*3,h*3), interpolation=cv2.INTER_CUBIC)
    resized_lanczos4 = cv2.resize(img, (w*3,h*3), interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow("cubic", resized_cubic)
    cv2.imshow("lanczos4", resized_lanczos4)
    cv2.waitKey(0)

def zad9():
    for scale in [1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0]:
        new_w = int(w * scale)
        new_h = int(h * scale)
        resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
        cv2.imshow(f"9 - Skala {int(scale * 100)}%", resized)
        cv2.waitKey(500)

def zad10():
    resized = imutils.resize(img, width=800)
    cv2.imwrite("resized_output.jpg", resized)

def main():
    zad1()

if __name__ == "__main__":
    main()
