import cv2, time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for x,y,width,height in face:
        img = cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 0, 67), 3)
        smile = smile_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=20)
        for x,y,width,height in smile:
            img = cv2.rectangle(frame, (x,y), (x+width, y+height), (0, 255, 0), 2)
            if len(smile)>1:
                cv2.putText(img, "Smiling", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3, cv2.LINE_AA)
    
    cv2.imshow('gotcha', frame)
    key = cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows