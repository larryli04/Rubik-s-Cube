from func import toArduino
import sys
sys.path.append("./RubiksCube-TwophaseSolver")

import colordetect as cd
import solver as sv
import const

# # get string from color detection
# string = cd.detect()
# cubestring = ""
# for char in string:
#     cubestring+=const.face[char]

# testing cubestring
cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
print(cubestring)

a = sv.solve(cubestring, 20, 2)
print(a)

# convert a to arduino-compatible number and send to arduino
print(toArduino(a))
# func.rotate(toArduino(a))
