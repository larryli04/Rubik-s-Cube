import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import func
import const

vid = cv2.VideoCapture(1) # initialize camera object
cubelist = [""] * 54 # define cube datatype

def detect():
    

    for face in range(3): # 3 faces to turn
        for rotation in range(4): # 4 turns per face
            
            ret,frame = vid.read() # get picture
            frame = cv2.resize(frame, (640,480))

            while(True): # wait for key
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            for x in range(6): # 6 pixels per 3 cubelets per rotation
                cubelist[const.location[face][rotation][x]] = func.colorOf(const.visible(face)[x]) # color detection
            
            func.rotate(const.turns[face])

    middle =  [5, 14, 23, 32, 41, 50]
    for x in range(len(middle)):
        cubelist[const.location] = const.colors[x]

    print(cubelist)
    cube = "".join(cubelist) # turn the array "cubelist" into string
    print(cube)
    
    cv2.destroyAllWindows() # cv2 window cleanup
    return cube

if __name__ == "__main__":
    pass