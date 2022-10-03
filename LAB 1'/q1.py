list1=[1,2,3,4,5]
list2=[6,7,8,9,10,11]
finallist=[]

for i in list1:
    if(i%2!=0):
        finallist.append(i)


for i in list2:
    if(i%2==0):
        finallist.append(i)


print(finallist)
