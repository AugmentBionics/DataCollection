import serial
import csv

file = open('muscleRead.csv', 'wb')
wr = csv.writer(file)

port = serial.Serial("/dev/tty.usbmodem1411",9600)
data = []
flex_time = []

while(len(data)<1400):
    if len(data) >= 500 and len(data) <= 1000:
        flex_time.append('Flex')
        print("FLEX")
        
    else:
        flex_time.append('Not')
        print("STOP")
        
    data.append(port.readline())


wr.writerow(data)
wr.writerow(flex_time)
file.close()
