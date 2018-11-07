#!/usr/bin/python
import sys
import socket

print sys.argv[1]," ====> ",socket.gethostbyname(sys.argv[1])
