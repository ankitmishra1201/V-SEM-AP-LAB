#!/usr/bin/python         

import socket               

s = socket.socket()         
host = socket.gethostname() 
port = 12345                


s.connect((host, port))
string=str(input("Enter the String: "))
s.send(string.encode())
print(s.recv(1024).decode())



s.close()            