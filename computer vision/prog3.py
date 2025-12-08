import cv2

img = cv2.imread("image3.png")
new_img = img[100:220, 300:430]

print(img.shape)

cv2.imshow("image", img)
cv2.imshow("new image", new_img)

cv2.waitKey(0)
cv2.destoryAllWindows()