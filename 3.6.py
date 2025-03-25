import cv2

img = cv2.imread("3image.jpg")
(centerX, centerY) = (img.shape[1] // 2, img.shape[0] // 2)
#b
cv2.circle(img, (500, 370), 30,(0,0,255),-1)
cv2.circle(img, (680, 370), 30,(0,0,255),-1)
#c
cv2.rectangle(img, (500,500), (670, 570), (0, 255, 0), -1)
#d
cv2.circle(img, (centerX, centerY), 230, (255, 0, 0), 2)

cv2.imshow("6", img)
cv2.waitKey(0)