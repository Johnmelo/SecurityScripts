#!/usr/bin/python
import socket
import sys

#ip = raw_input("enter with ip address: ")
#porta = input("port number: ")
ip = None
start = 1
end = 65535
count = len(sys.argv)
if count >= 2:
	ip = sys.argv[1]
	if count >=3:
		start = sys.argv[2]
	if count >= 4:
		end = sys.argv[3]
	for port in range(int(start),int(end)):
                mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

                if mySocket.connect_ex((ip,port)) == 0:
                        print "port ",port," [OPEN]"
else:
	print "usage: ./portscan.py [TARGET_IP] [START PORT] [END PORT]"
