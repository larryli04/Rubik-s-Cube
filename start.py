import func
import cv2
import time
import sys
sys.path.append("./RubiksCube-TwophaseSolver")

import colordetect as cd
import solver as sv
import const

input() # wait for key

# get string from color detection
string = cd.detect()
cubestring = ""
for char in string:
    cubestring+=const.face[char]

# testing cubestring
# cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
# cubestring = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB' solved cube 
# cubestring = "YBGYYWWGRBRWWRWOGGBOYWBOBRWOBBRWRRGROOROOGGYYOYGBGBWYY"
print(cubestring)

a = sv.solve(cubestring, 20, 2)
print(a)

# convert a to arduino-compatible number and send to arduino
for item in func.toArduino(a):
    func.rotate(item)
    time.sleep(1)
# func.rotate(toArduino(a))
