#!/usr/bin/python
import socket
import sys

BUFFER_SIZE = 1024

if len(sys.argv) < 3:
	print "usage: ./getData TARGET_IP PORT"
else:
	ip = sys.argv[1]
	porta = sys.argv[2]
	mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	if mySocket.connect_ex((ip,int(porta))) == 0:
		print "porta aberta"
		data = mySocket.recv(BUFFER_SIZE)
		print "Dados recebidos ",data
