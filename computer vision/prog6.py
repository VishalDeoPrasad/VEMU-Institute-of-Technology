import cv2

img1 = cv2.imread("image4.png")
img2 = cv2.imread("image5.png")

img3 = cv2.addWeighted(img1, 0.2, img2, 0.8, 0)

cv2.imwrite("output.jpg", img3)
cv2.imshow("image3", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()