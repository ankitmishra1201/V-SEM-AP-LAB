def checkHex(s):
   
    
    for ch in s:
 
        
        if ((ch < '0' or ch > '9') and
            (ch < 'A' or ch > 'F')):
                 
            print("No")
            return
         
    
    print("Yes")


s = str(input("Enter Hexadecimal: "))
checkHex(s)
