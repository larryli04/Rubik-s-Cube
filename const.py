import numpy as np
import func


import serial

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

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
    [[220,160],[265,180],[330,190],[365,165],[411,125]], # top left to right
    [[206,203],[251,217],[300,245],[300,295],[300,340]], # left top to bottom
    [[340,341],[340,294],[349,239],[390,209],[430,175]]  # right bottom to top
]

location = [
    [[19,22,25,39,42,45],[25,26,27,28,29,30],[27,24,21,16,13,10],[21,20,19,9,8,7]],
    [[19,22,25,39,42,45],[1,4,7,37,38,39],[54,51,48,43,40,37],[28,31,34,45,44,43]],
    [[7,8,9,19,20,21],[9,6,3,10,11,12],[3,2,1,46,47,48],[1,4,7,37,38,39]]
]

lastThree = [
    [49,52,15,18],
    [17,18,33,36],
    [35,36,53,52]
]

lastVisible = [
    [[365,165],[411,125],[390,209],[430,175]],
    [[340,294],[340,341],[300,295],[300,340]],
    [[340,294],[340,341],[300,295],[300,340]]
]

def visible(face):
    if face==0 or face==1:
        list = func.Reverse(visible_cubes[2][:3])+(visible_cubes[1][2:])
        
        return list
    if face == 2:
        list = visible_cubes[0][2:]+(visible_cubes[2][2:])
        # plot(list)
        return list

print(visible(2))

colors = ["O", "B", "R", "G", "Y","W"] # list order of colors

turns = ["F","L","U"] # order of the faces to turn during the color detection BYO

face = {
    "W":"D",
    "O":"L",
    "G":"B",
    "R":"R",
    "B":"F",
    "Y":"U"
}

num_to_face = ["L","F","R","B","U","D"]