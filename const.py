import numpy as np
import func
import serial

# arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

boundaries = {
    
    "Y":((0, 80,80), (60, 150, 150)),
    "O":((0,40,153),(50,178,255)),
    "R":((0,0,200),(50, 50, 255)),
    
    "B":((153, 0, 0), (255, 102, 102)),
    "W":((192,192,192),(255,255,255)),
    "G":((0, 200, 0), (100,200,100)),
}
for element in boundaries: # turn all elements in boundaries to numpy array
    boundaries[element] = np.array([np.array(boundaries[element][0]), np.array(boundaries[element][1])])

visible_cubes = [
    [[220,160],[265,180],[343,201],[365,172],[411,147]], # top left to right
    [[206,203],[251,217],[320,265],[311,301],[314,340]], # left top to bottom
    [[358,341],[355,294],[349,239],[390,209],[427,180]]  # right bottom to top
]

location = [
    [[19,22,25,12,15,18],[25,26,27,46,47,48],[27,24,21,34,31,28],[21,20,19,9,8,7]],
    [[19,22,25,12,15,18],[1,4,7,10,11,12],[45,42,39,16,13,10],[46,49,52,18,17,16]],
    [[7,8,9,19,20,21],[9,6,3,28,29,30],[3,2,1,37,38,39],[1,4,7,10,11,12]]
]

def visible(face):
    if face==0 or face==1:
        list = func.Reverse(visible_cubes[2][:3])+(visible_cubes[1][2:])
        # func.plot(list)
        return list
    if face == 2:
        list = visible_cubes[0][2:]+(visible_cubes[2][2:])
        return list

colors = ["W", "O", "G", "R", "B", "Y"] # list order of colors

turns = ["F","L","U"]

arduino_conv = { #adjusted to the wiring
    "U": 0,
    "L": 1,
    "F": 2,
    "R": 3,
    "B": 4,
    "D": 5
}

face = {
    "W":"U",
    "O":"L",
    "G":"F",
    "R":"R",
    "B":"B",
    "Y":"D"
}