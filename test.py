import serial
import csv

file = open('muscleRead.csv', 'wb')
wr = csv.writer(file)

port = serial.Serial("/dev/tty.usbmodem1411",9600)
data = []
flex_time = []
l = 0

while(l < 10000):
    if l <= 3000 and l >= 8000:
        flex_time.append('Flex')
    else:
        flex_time.append('Not')
        
    data.append(port.readline())
    l += 1




wr.writerow(data)
wr.writerow(flex_time)
file.close()
