import cv2
import imutils
img = cv2.imread("5image.jpg")
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated_cv = cv2.warpAffine(img, M, (w, h))

rotated_imutils = imutils.rotate(img, 60)

cv2.imshow("OpenCV", rotated_cv)
cv2.imshow("imutils", rotated_imutils)
cv2.waitKey(0)