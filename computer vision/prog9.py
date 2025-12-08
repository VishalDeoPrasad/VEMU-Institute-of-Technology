import cv2

img = cv2.imread("image7.png")
edge = cv2.Canny(img, 100, 200)

cv2.imshow("image", img)
cv2.imshow("Edge", edge)

cv2.waitKey(0)
cv2.destroyAllWindows()