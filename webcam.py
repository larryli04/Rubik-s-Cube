import cv2
import pyautogui as p
import numpy as np
import const
import func

boundaries = {
    
    "Y":((0, 80,80), (60, 150, 150)),
    "O":((0,40,153),(50,178,255)),
    "R":((0,0,200),(50, 50, 255)),
    
    "B":((153, 0, 0), (255, 102, 102)),
    "W":((192,192,192),(255,255,255)),
    "G":((0, 200, 0), (100,200,100)),
}

visible_cubes = [
    [[220,160],[265,180],[343,201],[365,172],[411,147]], # top left to right
    [[206,203],[251,217],[300,265],[311,301],[314,340]], # left top to bottom
    [[358,341],[355,294],[349,239],[390,209],[427,180]]  # right bottom to top
]

def transform(color):
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
    # if(output)
    
    return np.array([255,255,255])

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    while(True):
        ret_val, img = cam.read()
        img = cv2.resize(img, (640,480))
        x, y = p.position()
        
        for i in range(6):
            cv2.circle(img,(const.visible(2)[i][0],const.visible(2)[i][1]),4,(255,0,0),-1)
        
        try:
            
            pixel = img[y-30][x-10]
            print(x, y,"color:", func.colorOf(pixel), pixel)
            
            
        except:
            # print("None")
            pass
        cv2.imshow("", img)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()