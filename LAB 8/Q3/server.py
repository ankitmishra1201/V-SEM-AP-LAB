import socket              

s = socket.socket()        
host = socket.gethostname() 
port = 12345               
s.bind((host, port))        

s.listen(5)                
while True:
   c, addr = s.accept()     
   print( 'Got connection from', addr)
   string=c.recv(1024).decode()
   if(string==string[::-1]):
      c.send("String is Pallindrome with length ".encode())
   else:
        c.send("String is not pallindrome with length ".encode())

   length=len(string)
   c.send(str(length).encode())


   c.close()    