# -*- coding: utf-8 -*-
"""
read gsr file from gsr sensor raspberry pi
"""
import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import serial.tools.list_ports as list_ports
import sys
file_name = 'gsr.txt'
record_time = 10 # length of the trail in second
serialPort = None
usingPorts = list(list_ports.comports())
for port in usingPorts:
    #debug to detect Serial name
    print(port.description)
    if sys.platform.startswith('win'):
        if "Serial" in port.description:
            serialPort = port.device
            break
        # end
    elif sys.platform.startswith('darwin'):
        if "IOUSBHostDevice" in port.description:
            serialPort = port.device
            break
        # end
    # end
# end
# set up the serial line
ser = serial.Serial(serialPort, 57600)
time.sleep(3)


start_time = time.time()
# Read and record the data
data =[]                       # empty list to store the data
while time.time() - start_time < record_time:
    b = ser.readline()         # read a byte string
    string_n = b.decode()      # decode byte string into Unicode  
    string = string_n.rstrip() # remove \n and \r

    try:
        ppg = float(string)    # convert string to float
    except:
        continue
    
    time_cur = time.time() - start_time
    new_line = [time_cur, ppg]
    print('Time: ' + str(time_cur))
    

    data.append(new_line)           # add to the end of data list

ser.close()

data_array = np.array(data)
print('Record ended, data shape: ' + str(data_array.shape))
print('Data saved at:' + file_name)
np.savetxt(file_name, data_array)