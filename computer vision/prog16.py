import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    blur_frame = cv2.GaussianBlur(frame, (61,61), 0)

    faces = face_cascade.detectMultiScale(frame)
    for face in faces:
        (x,y,w,h) = face
        frame[y:y+h, x:x+h] = blur_frame[y:y+h, x:x+h]

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()