from audioop import reverse
from re import search
import socket 
import json             

s = socket.socket()        
host = socket.gethostname() 
port = 1238
s.bind((host, port))        

s.listen(5)                
while True:
   c, addr = s.accept()     
   print( 'Got connection from', addr)
   ch=c.recv(1024).decode()
   print(ch)
   list=c.recv(1024).decode()
   list=json.loads(list)
   print(list)

   if(int(ch)==1):
      search=int(c.recv(1024).decode())
      for i in range(len(list)):
         if(list[i]==search):
           c.send("Number is found in index: ".encode())
           c.send(str(i).encode())
   elif(int(ch)==2):
      sort_ch=int(c.recv(1024).decode())
      if(sort_ch==1):
        list.sort()
        list=json.dumps(list)

        c.send(list.encode())
      elif(sort_ch==2):
         list.sort(reverse=True)
         list=json.dumps(list)
         c.send(list.encode())
   elif(int(ch)==3):
      odd_list=[]
      even_list=[]
      for i in list:
         if(i%2==0):
            even_list.append(i)
         else:
            odd_list.append(i)
      odd_list=json.dumps(odd_list)
      even_list=json.dumps(even_list)
      c.send(odd_list.encode())
      c.send(even_list.encode())
   elif(int(ch)==4):
      c.close()

      


         
      




   


   c.close()    