import cv2

eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
img = cv2.imread("image8.png")

eyes = eye_cascade.detectMultiScale(img)
for eye in eyes:
    (x, y, w, h) = eye
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()