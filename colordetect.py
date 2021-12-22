import cv2
import numpy as np
import time
import matplotlib.pyplot as plt
import func
import const

vid = cv2.VideoCapture(0) # initialize camera object
cubelist = [""] * 54 # define cube datatype

def detect():
    

    for face in range(3): # 3 faces to turn
        for rotation in range(4): # 4 turns per face
            
            
            # for x in range(6):
            #     cv2.circle(frame,(const.visible(face)[x][0],const.visible(face)[x][1]),4,(255,0,0),-1)
            while(True): # wait for key
                ret,frame = vid.read() # get picture
                frame = cv2.resize(frame, (640,480))
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
            for x in range(6): # 6 pixels per 3 cubelets per rotation
                print(const.visible(face)[x][0],const.visible(face)[x][1],func.colorOf(frame[const.visible(face)[x][1]][const.visible(face)[x][0]]))
                cubelist[const.location[face][rotation][x]-1] = func.colorOf(frame[const.visible(face)[x][1]][const.visible(face)[x][0]]) # color detection
            
            func.rotate(const.turns[face])
            time.sleep(1)
            print("turned!")

    while(True): # wait for key
                ret,frame = vid.read() # get picture
                frame = cv2.resize(frame, (640,480))
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    #determine the last 9 slots on the back of the cube
    # R' U then look at [365,165],[411,125] and [390,209],[430,175]
    func.rotate("R")
    time.sleep(1)
    func.rotate("R")
    time.sleep(1)
    func.rotate("R")
    time.sleep(1)
    func.rotate("U")
    while(True): # wait for key
                ret,frame = vid.read() # get picture
                frame = cv2.resize(frame, (640,480))
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    for x in range(4):
        print(const.lastThree[0][x]-1)
        cubelist[const.lastThree[0][x]-1] = func.colorOf(frame[const.lastVisible[0][x][1]][const.lastVisible[0][x][0]])
    print(cubelist)
    func.rotate("U")
    time.sleep(1)
    func.rotate("U")
    time.sleep(1)
    func.rotate("U")
    time.sleep(1)
    func.rotate("R")

    # D' F then look at [300,295],[300,340] and [340,341],[340,294]
    func.rotate("D")
    time.sleep(1)
    func.rotate("D")
    time.sleep(1)
    func.rotate("D")
    time.sleep(1)
    func.rotate("F")
    while(True): # wait for key
                ret,frame = vid.read() # get picture
                frame = cv2.resize(frame, (640,480))
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    for x in range(4):
        print(const.lastThree[1][x]-1)
        cubelist[const.lastThree[1][x]-1] = func.colorOf(frame[const.lastVisible[1][x][1]][const.lastVisible[1][x][0]])
    func.rotate("F")
    time.sleep(1)
    func.rotate("F")
    time.sleep(1)
    func.rotate("F")
    time.sleep(1)
    func.rotate("D")

    # D L' then look at [300,295],[300,340] and [340,341],[340,294]
    func.rotate("D")
    time.sleep(1)
    func.rotate("L")
    time.sleep(1)
    func.rotate("L")
    time.sleep(1)
    func.rotate("L")
    while(True): # wait for key
                ret,frame = vid.read() # get picture
                frame = cv2.resize(frame, (640,480))
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
    for x in range(4):
        cubelist[const.lastThree[2][x]-1] = func.colorOf(frame[const.lastVisible[2][x][1]][const.lastVisible[2][x][0]])
    func.rotate("L")
    time.sleep(1)
    func.rotate("D")
    time.sleep(1)
    func.rotate("D")
    time.sleep(1)
    func.rotate("D")

    middle =  [41, 23, 14, 50, 5, 32]
    for x in range(len(middle)): # TODO make sure this matches the standard
        cubelist[middle[x]-1] = const.colors[x]

    print(cubelist)
    cube = "".join(cubelist) # turn the array "cubelist" into string
    print(cube)
    
    cv2.destroyAllWindows() # cv2 window cleanup
    return cube

if __name__ == "__main__":
    pass
    print(detect())