import serial
import csv
from sys import argv
from time import sleep

file1 = open('{}_{}_{}_v1.csv'.format(argv[1], argv[2], argv[3]), 'wb')
file2 = open('{}_{}_{}_v2.csv'.format(argv[1], argv[2], argv[3]), 'wb')


port = serial.Serial("/dev/tty.usbmodem1421",9600)
data = []
flex_time = []

wr = csv.writer(file1)

while(len(data)<1400):
    if len(data) >= 500 and len(data) <= 1000:
        flex_time.append('Flex')
        print("FLEX")
        
    else:
        flex_time.append('Not')
        print("STOP")
        
    data.append(port.readline())
    sleep(0.01)
    
wr.writerow(data)
wr.writerow(flex_time)
file1.close()


data = []
flex_time = []
wr = csv.writer(file2)
while(len(data)<1400):
    if len(data) >= 500 and len(data) <= 1000:
        flex_time.append('Flex')
        print("FLEX")
        
    else:
        flex_time.append('Not')
        print("STOP")
        
    data.append(port.readline())
    sleep(0.01)

wr.writerow(data)
wr.writerow(flex_time)
file2.close()
