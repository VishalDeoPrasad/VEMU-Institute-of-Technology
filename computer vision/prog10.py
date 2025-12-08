import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("image9.png")

faces = face_cascade.detectMultiScale(img)
print(len(faces))

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()