import os
import time
import cv2
import numpy as np

# table = "Ñ@#W$9876543210?!abc;:+=-,._"
table = "@%#*+=-:,. "
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Couldn't open camera")
    exit()

while True:
    os.system('cls')
    ret, frame = cap.read()
    if not ret:
        print("can't receive frame, exiting....")
        break

    cv2.imshow("Live Cam Feed", frame)
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    width = 100
    height = int(frame.shape[0] * (width / frame.shape[1]) * 0.5)
    frame_gray = cv2.resize(frame_gray, (width, height))
    
    img_ascii = ""
    for i in range(frame_gray.shape[0]):
        for j in range(frame_gray.shape[1]):
            img_ascii += table[int(frame_gray[i][j] / 255 * (len(table)-1))]
        img_ascii += "\n"
    
    print(img_ascii)
    
    
    if cv2.waitKey(1) == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()