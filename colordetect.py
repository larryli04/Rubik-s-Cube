import cv2
import numpy as np
import serial
import time

# U1, U2, U3, U4, U5, U6, U7, U8, U9, R1, R2,
# R3, R4, R5, R6, R7, R8, R9, F1, F2, F3, F4, F5, F6, F7, F8, F9, D1, D2, D3, D4, D5, D6, D7, D8, D9, L1, L2, L3, L4,
# L5, L6, L7, L8, L9, B1, B2, B3, B4, B5, B6, B7, B8, B9

# The names of the facelet positions of the cube
#                   |************|
#                   |* 1** 2** 3*|
#                   |************|
#                   |* 4** 5** 6*|
#                   |************|
#                   |* 7** 8** 9*|
#                   |************|
#      |************|************|************|************|
#      |*10**11**12*|*19**20**21*|*28**29**30*|*37**38**39*|
#      |************|************|************|************|
#      |*13**14**15*|*22**23**24*|*31**32**33*|*40**41**42*|
#      |************|************|************|************|
#      |*16**17**18*|*25**26**27*|*34**35**36*|*43**44**45*|
#      |************|************|************|************|
#             camera|************|
#                   |*46**47**48*|
#                   |************|
#                   |*49**50**51*|
#                   |************|
#                   |*52**53**54*|
#                   |************| 

boundaries = {
    "R":([153,0,0], [255, 102, 102]),
    "G":([0, 153, 0], [102,255,102]),
    "B":([0, 0, 153], [102, 102, 255]),
    "O":([153,76,0],[255,178,102]),
    "Y":([153, 153, 0], [255, 255, 153]),
    "W":([192,192,192],[255,255,255]),
}

pixel = [[],[],[]]

CWISE = 1
ACWISE = 0

arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

location = [
    [[12,19,15,22,18,25],[46,25,47,26,48,27],[34,27,31,24,28,21],[9,21,8,20,7,19]],
    [[12,19,15,22,18,25],[10,1,11,4,12,7],[16,45,13,42,10,39],[18,46,17,49,16,52]],
    [[46,25,47,26,48,27],[52,16,49,17,48,18],[54,3,53,2,52,1],[48,34,51,35,54,36]]
]
turns = ["F","L","D"]

def colorOf(color):
    for key in boundaries:
        if (cv2.inRange(color,boundaries[key][0], boundaries[key][1])):
            return key

def rotate(face, direction):
    # face is 0-5
    # direction is 0 or 1
    arduino.write(bytes(face, 'utf-8'))
    arduino.write(bytes(direction, 'utf-8'))

for face in range(3): # 3 faces to turn
    for rotation in range(4): # 4 turns per face
        # get a picture of the state
        vid = cv2.VideoCapture(1)
        cubelist = [""] * 54

        ret,frame = vid.read()
        while(True):
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # read pixels

        # put them at place
        for x in range(6):
            color = colorOf(pixel[face][x])
            cubelist[location[face][rotation][x]] = color
        # rotate to next
        # rotate(turns[face])
    # reset face
    # rotate(turns[face])

cube = "".join(cubelist)
vid.release()

cv2.destroyAllWindows()