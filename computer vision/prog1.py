import cv2

img = cv2.imread("image2.png")
print(img.shape)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()