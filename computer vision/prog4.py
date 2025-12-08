import cv2
import numpy as np

img = np.ones((400, 400, 3), dtype=np.uint8)
cv2.line(img, (50, 50), (350, 50), (145, 200, 155), 10)
cv2.rectangle(img, (50,100), (170,200), (0,0,255), 10)
cv2.rectangle(img, (230,100), (350,200), (0,0,255), 10)
points = np.array([[150, 250], [250,250], [200, 300]])
points = points.reshape((-1, 1, 2))
# cv2.polylines(img, [points], True, (0,255,255), 10)
cv2.fillPoly(img, [points],(0,255,255))

cv2.circle(img, (200, 350), 40, (14,100,255), 10)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()