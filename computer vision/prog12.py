import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("image9.png")
blur_img = cv2.GaussianBlur(img, (41,41), 0)

faces = face_cascade.detectMultiScale(img)

for face in faces:
    (x, y, w, h) = face
    blur_img[y:y+h, x:x+w] = img[y:y+h, x:x+w]

cv2.imshow("blur", blur_img)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()