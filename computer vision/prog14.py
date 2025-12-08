import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, 50, 150)

    cv2.imshow("Frame", frame)
    cv2.imshow("gray", gray)
    cv2.imshow("edge", edge)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()