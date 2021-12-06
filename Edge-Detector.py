import cv2
import numpy as np

filename = 'damatahtasi.jpg'

while(1):

    frame = cv2.imread(filename)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Orjinal',frame)
    kenar = cv2.Canny(frame,100,200)
    cv2.imshow('Kenarlari',kenar)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()