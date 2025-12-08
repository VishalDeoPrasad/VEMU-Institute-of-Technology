import cv2

img = cv2.imread("image3.png")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("hsv", hsv_img)
cv2.imshow("gray", gray_img)
cv2.imshow("rgb", rgb_img)
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyallWindows()