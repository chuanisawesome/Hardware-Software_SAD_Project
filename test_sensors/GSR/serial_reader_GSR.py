# -*- coding: utf-8 -*-
"""
read gsr file from gsr sensor raspberry pi
"""
import serial
import time
import numpy as np
#import matplotlib.pyplot as plt
import serial.tools.list_ports as list_ports
import sys
#file_name = 'gsr.txt'
record_time = 500 # length of the trail in second

# set up the serial line
#ser = serial.Serial(serialPort, 57600)
ser = serial.Serial('/dev/ttyACM0', 9600)


start_time = time.time()
# Read and record the data
data =[]                       # empty list to store the data
while time.time() - start_time < record_time:
    b = ser.readline()         # read a byte string
    
    string_n = b.decode()      # decode byte string into Unicode  
    b = b.rstrip() # remove \n and \r
    data.append(b)           # add to the end of data list\
    print(b)
    print(data)
    try:
        gsr = float(b)# convert string to float
        print(gsr)
    except:
        continue
    
#    time_cur = time.time() - start_time
#    print('Time: ' + str(time_cur))

ser.close()

#data_array = np.array(data)
#print('Record ended, data shape: ' + str(len(data)))
#print('Data saved at:' + file_name)
print(data)

file = open("gsr.txt", "w+")
content = str(data)
file.write(content)
file.close()

#np.savetxt(file_name, data)