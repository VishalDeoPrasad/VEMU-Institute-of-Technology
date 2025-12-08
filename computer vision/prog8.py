import cv2
import numpy as np

img = cv2.imread("image3.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100,150,0])
upper_blue = np.array([140,255,255])

mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
blue = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("blue", blue)
cv2.imshow("mask", mask)
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()