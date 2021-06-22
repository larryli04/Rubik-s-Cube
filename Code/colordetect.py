import cv2
import numpy as np

boundaries = {
    "red":([153,0,0], [255, 102, 102]),
    "green":([0, 153, 0], [102,255,102]),
    "blue":([0, 0, 153], [102, 102, 255]),
    "orange":([153,76,0],[255,178,102]),
    "yellow":([153, 153, 0], [255, 255, 153]),
    "white":([192,192,192],[255,255,255]),
}

def colorOf(color):
    for key in boundaries:
        if (cv2.inRange(color,boundaries[key][0], boundaries[key][1])):
            return key

# get a picture of the state
vid = cv2.VideoCapture(1)
cubelist = [""] * 54

ret,frame = vid.read()
while(True):
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# read pixels
color = colorOf(pixel)
# put them at place
cubelist
# rotate to next

cube = "".join(cubelist)
vid.release()

cv2.destroyAllWindows()