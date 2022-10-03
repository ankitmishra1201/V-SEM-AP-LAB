#!/usr/bin/python         

import socket
import json               

s = socket.socket()         
host = socket.gethostname() 
port = 1238            


s.connect((host, port))
while True:
   print("Select the choice ")
   print("(1) Search a number")
   print("(2) Ascending/descending")
   print("(3)Split to odd/even")
   print("(4) Close")
  
   ch=int(input("Enter the choice\n "))
   s.send(str(ch).encode())
   n=int(input("Enter the size of list "))
   list=[]
   for i in range(n):
      y=int(input())
      list.append(y)

   encoded_list=json.dumps(list)
   s.send(encoded_list.encode())

   if(ch==1):
      search=int(input("Enter the value to be searched: "))
      s.send(str(search).encode())
      print(s.recv(1024).decode())
   elif(ch==2):
      sort_ch=int(input("(1)Ascending/(2)Descending. Enter the choice\n"))
      s.send(str(sort_ch).encode())
      list=s.recv(1024).decode()
      list=json.loads(list)
      print(list)
   elif(ch==3):
      odd_list=s.recv(1024).decode()
      #odd_list=json.loads(odd_list)
      print(odd_list)
      print()
      even_list=s.recv(1024).decode()
      #even_list=json.loads(even_list)
      print(even_list)
   elif(ch==4):
      s.close()






   

   
   
   
  



  
  
  

        