import matplotlib.pyplot as plt
import numpy as np
import const

def Reverse(lst):
    lst.reverse()
    return lst

def plot(list):
    print(list)
    x = []
    y=[]
    for i in range(len(list)):
        x.append(list[i][0])
        y.append(list[i][1])
    print(x,y)
    plt.plot(x,y)
    plt.axis("equal")
    plt.show()

def rotate(face):
    # rotate face clockwise
    const.arduino.write(bytes(face, 'ascii'))

def transform(color): # color processing to make boundary detection easier and more reliable
    output = np.int16(color)
    #print(output)
    
    if(output[2]-output[1]>=70):
        if(output[2]-output[0] >= 70): # REDNESS
            if(output[1]-output[0] > 30): #ORANGE
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
    if(abs(output[2]-output[1]) < 40): # YELLOW
        if(output[2]-output[0] > 10):
            return np.array([30,100,100])
    if(output[1] > (output[2]+output[0])-20): #GREEN
        return (100,200,100)
    if((abs(output[1] - output[0]) < 80) and (abs(output[2] - output[1]) < 60)): # WHITE
        return np.array([255,255,255])
    
    return np.array([255,255,255])

def colorOf(color): # compare the pixel read from camera to color definitions
    pixel = transform(color) #color processing
    
    for key in const.boundaries:
        
        if((pixel>=const.boundaries[key][0]).all() and (pixel<=const.boundaries[key][1]).all()): # complare pixel
            return key
    return "No Color Detected"

def toArduino(solution): # gets solution string and returns int to be sent to arduino
    sarray = solution.split(" ")[:-1]
    
    print(sarray)
    out_array = []
    for elem in sarray:
        x = int(elem[1])
        for i in range(x):
            out_array.append(elem[0])
    
    print("Output to Arduino:", out_array)
    return out_array


