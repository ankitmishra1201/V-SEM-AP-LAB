#Armstrong number


n=int(input("Enter the number:" ))

sum=0

temp=n

while(temp>0):
    digit=temp%10
    sum=sum+digit*digit*digit
    temp=temp//10



if(sum==n):
    print("Its an armstrong number")
else:
    print("Its not an armstrong number")

    
    



















































