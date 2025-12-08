import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame)
    for face in faces:
        (x, y, w, h) = face
        print((x, y, w, h))
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()