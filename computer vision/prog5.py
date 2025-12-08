import cv2

img = cv2.imread("image3.png")
cv2.rectangle(img, (300,100), (430,230), (0,255,0), 6)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()