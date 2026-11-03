import cv2

cap = cv2.VideoCapture("videos/metro1.mp4")

ret, frame = cap.read()
print(ret)

if ret:
    cv2.imwrite("frame.jpg", frame)
    print("Frame saved!")
else:
    print("Couldn't read frame.")

cap.release()