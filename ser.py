from cv2 import rectify3Collinear
import serial
import time
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
time.sleep(2)

def getValues():
    arduinoData = arduino.readline().decode('utf-8')
    return arduinoData
while(True):
    # out = int(input())
    # arduino.write(bytes(out))

    # time.sleep(0.5)
    userInput = input('input:')
    arduino.write(bytes(userInput,"ascii"))
    print(getValues())

    # need to output letter of face to Serial line
    # arduino.write(bytes(face,"ascii"))