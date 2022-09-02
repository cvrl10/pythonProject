
print('this is ', __name__)



import socket
import os
print(os.cpu_count())

name = 'Carl'

byte = name.encode('ASCII')

print(byte)
print(byte.decode('koi8_r'))