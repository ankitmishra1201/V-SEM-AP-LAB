m=int(input('Enter starting number'))
n=int(input('Enter ending number'))
primelist=[]

for val in range(m,n):
    if val>1:
        for i in range(2,val):
            if(val%i)==0:
                break
        else:
          primelist.append(val)


print(primelist)

