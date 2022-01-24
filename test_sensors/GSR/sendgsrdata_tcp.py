import math
import sys
import time
import socket
from grove.adc import ADC


HOST = 'change to remotehost ipaddr'    # The remote host
PORT = 50007              # The same port as used by the server

# is called each time the sensor value is read (add .encode())
def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data)

class GroveGSRSensor:

    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def GSR(self):
        value = self.adc.read(self.channel)
        return value

def main():
    Grove = GroveGSRSensor

    if len(sys.argv) < 2:
        print('Usage: {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)

    sensor = GroveGSRSensor(int(sys.argv[1]))

    print('Detecting...')
    while True:
        print('GSR value: {0}'.format(sensor.GSR))
        send_data('GSR value: {0}\n'.format(sensor.GSR))
        time.sleep(.3)

if __name__ == '__main__':
    main()