import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("image.png")
faces = face_cascade.detectMultiScale(img)
if len(faces) >= 2:
    (x1, y1, w1, h1) = faces[0]
    (x2, y2, w2, h2) = faces[1]

    face1 = img[y1:y1 + h1, x1:x1 + w1]
    face1_resized = cv2.resize(face1, (w2, h2))

    face2 = img[y2:y2 + h2, x2:x2 + w2]
    face2_resized = cv2.resize(face2, (w1, h1))

    frame_swap = img.copy()
    frame_swap[y2:y2 + h2, x2:x2 + w2] = face1_resized
    frame_swap[y1:y1 + h1, x1:x1 + w1] = face2_resized

    cv2.rectangle(frame_swap, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)
    cv2.rectangle(frame_swap, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)
    cv2.imshow("face swap", frame_swap)
    cv2.imshow("original image", img)
else:
    cv2.imshow("face swap", img)
    
cv2.waitKey(0)
cv2.destroyAllWindows()