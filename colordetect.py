import cv2
import numpy as np
import serial
import time

# TODO:
# programmatic search for the right numbers in visible cubes
# change location variable to account for new camera position
# cleanup and annotation

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
#             camera|************|
#      |************|************|************|************|
#      |*10**11**12*|*19**20**21*|*28**29**30*|*37**38**39*|
#      |************|************|************|************|
#      |*13**14**15*|*22**23**24*|*31**32**33*|*40**41**42*|
#      |************|************|************|************|
#      |*16**17**18*|*25**26**27*|*34**35**36*|*43**44**45*|
#      |************|************|************|************|
#                   |************|
#                   |*46**47**48*|
#                   |************|
#                   |*49**50**51*|
#                   |************|
#                   |*52**53**54*|
#                   |************| 

colors = ["Y", ""] # list order of colors
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
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

visible_cubes = [
    [[220,160],[265,180],[343,201],[365,172],[411,147]], # top left to right
    [[206,203],[251,217],[320,265],[311,301],[314,340]], # left top to bottom
    [[358,341],[355,294],[349,239],[390,209],[427,180]]  # right bottom to top
]

def visible(face):
    if face==0 or face==1:
        return visible_cubes[2][:3][::1].append(visible_cubes[1][2:])
    if face == 2:
        return visible_cubes[0][2:].append(visible_cubes[2][2:])
    
    
CWISE = 0
ACWISE = 1



location = [
    [[19,22,25,12,15,18],[25,26,27,46,47,48],[27,24,21,34,31,28],[21,20,19,9,8,7]],
    [[19,22,25,12,15,18],[1,4,7,10,11,12],[45,42,39,16,13,10],[46,49,52,18,17,16]],
    [[7,8,9,19,20,21],[9,6,3,28,29,30],[3,2,1,37,38,39],[1,4,7,10,11,12]]
]
turns = ["F","L","U"]

def transform(color): # color processing to make boundary detection easier and more reliable
    output = np.int16(color)
    
    
    if(output[2]-output[1]>=70):
        if(output[2]-output[0] >= 70): # REDNESS
            if(output[1]-output[0] > 10): #ORANGE
                    return np.array([10,100,200])
    
    for x in range(len(output)):
        
        if output[x]<=25:
            output[x] = 0
        if output[x]>=230:
            output[x] = 255

    if(output[2]-(output[1]+output[0]) >= 60): # RED
        
        return np.array([0,0,255])
    if(output[0]-(output[2]+output[1]) >= 20): # BLUE
        return np.array([255,0,0])
    if(abs(output[2]-output[1]) < 50): # YELLOW
        if(output[2]-output[0] > 10):
            return np.array([30,100,100])
    if(abs(output[1]>(output[0]+output[2]))): #GREEN
        return (100,200,100)
    if((abs(output[1] - output[0]) < 80) and (abs(output[2] - output[1]) < 60)): # WHITE
        return np.array([255,255,255])
    
    return np.array([255,255,255])

def colorOf(color): # compare the pixel read from camera to color definitions
    
    pixel = transform(color)

    for key in boundaries:

        if((pixel>=boundaries[key][0]).all() and (pixel<=boundaries[key][1]).all()):
            return key
    return "No Color Detected"

vid = cv2.VideoCapture(1) # initialize camera object
cubelist = [""] * 54 # define cube datatype

def rotate(face, direction): #rotate a specific face in a direction by serial command to arduino
    # CONVENTIONS
    # face is 0-5 
    # direction is 0 (clockwise) or 1 (counterclockwise) ALWAYS CLOCKWISE
    arduino.write(bytes(face, 'utf-8'))

def send(message):
    arduino.write(bytes(message, 'utf-8'))
def detect():
    

    for face in range(3): # 3 faces to turn
        for rotation in range(4): # 4 turns per face
            # get a picture of the state
            
            ret,frame = vid.read()
            frame = cv2.resize(frame, (640,480))
            while(True):
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # read pixels

            # put them at place
            for x in range(6):
                
                cubelist[location[face][rotation][x]] = colorOf(visible(face)[x]) # programmatically search for the right pixel to look at
            # rotate to next
            rotate(turns[face])

    middle =  [5, 14, 23, 32, 41, 50]
    for x in range(len(middle)):
        cubelist[location] = colors[x]

    print(cubelist)
    cube = "".join(cubelist) # turn the array "cubelist" into string
    print(cube)

    cv2.destroyAllWindows() # cv2 window cleanup