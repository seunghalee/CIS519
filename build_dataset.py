# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:51:24 2017

@author: Adam
"""

"""
G0 - Curls
G1 - Lat raises
G2 - Shoulder press
G3 - Chest press
"""

import serial
import msvcrt
import numpy as np
import struct
import matplotlib.pyplot as plt

""" Setup Serial Connection with BLE-USB Adapter """
ser = serial.Serial(port = 'COM8', baudrate = 115200, bytesize = serial.EIGHTBITS)       #initialize pySerial

""" Initialize Communication """
serial_data = ""                    #create serial input data buffer
console_data = ""                   #create console input data buffer
G = 0                              #set current gesture to 0
num_gestures = 4                   #set total number of gestures
R = 0
num_reps = 10
X = np.zeros((1,3));
""" Begin Recording Gestures """
print("Begin recording")
#while(L < num_gestures):
#    """ Record gesture L """
    #input("Press any key to record Gesture " + str(L))
n = 0

while(G < num_gestures):
    while(R < num_reps):
        X = np.zeros((1,3));
        print("Press CTRL+C to begin recording G"+str(G) + " R" + str(R))
        try:
            while(1):
                pass
        except KeyboardInterrupt:
            pass
        try:
            while(1):
                ser.flushInput()
                serial_data = ser.readline().strip().split(",")
                while len(serial_data) < 3 or serial_data[0] == '' or serial_data[1] == '' or serial_data[2] == '':
                    serial_data = ser.readline().strip().split(",")
                serial_data = [int(serial_data[0]),int(serial_data[1]),int(serial_data[2])]
                #print(np.array(serial_data))
                #X = np.append(X,np.reshape(np.array(struct.unpack("6h",serial_data)),(2,3)),axis=0)
                X = np.vstack( (X , np.array(serial_data)) )
        except KeyboardInterrupt:
            pass
        np.savetxt(str(G)+"_"+str(R)+".csv", X, delimiter=",")  #save rep into file
        print("Saved: " + str(X.shape))
        R = R+1
    R = 0
    G = G+1
ser.close()
#print(X.shape)
#plt.plot(X[:,0])
#plt.plot(X[:,1])
#plt.plot(X[:,2])
