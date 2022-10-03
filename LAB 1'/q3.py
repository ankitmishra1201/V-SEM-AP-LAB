n=int(input(' Enter the number of strtings'))


strings=[]

#part 1

for i in range(n):
    word=(input('Enter the String: '))
    strings.append(word)

print(strings)


#part2

count=0
for i in strings:
    if(len(i)>=2 and (i[0]==i[-1])):
        count=count+1

print(count)



#PART 3

oddstrings=[]
for i in strings:
    if(len(i)%2!=0):
        oddstrings.append(i)


print(oddstrings)
