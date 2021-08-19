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

def rotate(message):
    # rotate face clockwise
    const.arduino.write(bytes(message, 'utf-8'))

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
    pixel = transform(color) #color processing

    for key in const.boundaries:
        if((pixel>=const.boundaries[key][0]).all() and (pixel<=const.boundaries[key][1]).all()): # complare pixel
            return key
    return "No Color Detected"

def toArduino(solution): # gets solution string and returns int to be sent to arduino
    sarray = solution.split(" ")
    sarray = sarray[:-1]
    
    out_array = 0
    for elem in sarray:
        x = int(elem[1])
        for i in range(x):
            out_array *= 10
            out_array += const.arduino_conv[elem[0]]
    print("Output to Arduino:", out_array)
    return out_array
    
