import sys
sys.path.append("C:/Users/Larry/Documents/Code/Rubik's Cube/Code/RubiksCube-TwophaseSolver")

import solver as sv
import cv2
import serial

# cam = cv2.VideoCapture(0)

# s, img = cam.read() # take image

# do some computer vision magic
# find the colors and add them to string of shape: 
# "YYYYYYYYYBBBBBBBBBRRRRRRRRRGGGGGGGGGOOOOOOOOOWWWWWWWWW"

def toArduino(solution): # gets solution string and returns int to be sent to arduino
    sarray = solution.split(" ")
    sarray = sarray[:-1]
    print(sarray)
    out_array = 0
    for elem in sarray:
        x = int(elem[1])
        for i in range(x):
            out_array *= 10
            out_array += arduino_conv[elem[0]]
    print("bitch")
    return out_array
    

arduino_conv = { #adjusted to the wiring
    "U": 0,
    "L": 1,
    "F": 2,
    "R": 3,
    "B": 4,
    "D": 5
}
face = {
    "Y":"U",
    "B":"L",
    "R":"F",
    "G":"R",
    "O":"B",
    "W":"D"
}

string = "YBR"
cubestring = ""
for char in string:
    cubestring+=face[char]
cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
print(cubestring)
# print(solver.solve(cubestring=cubestring))
a = sv.solve(cubestring, 20, 2)
print(a)

# convert a to arduino-compatible number and send to arduino

#testcode
print(toArduino(a))