matrices1=[]
matrices2=[]
matrices3=[]

m=int(input("Enter the number of rows"))
n=int(input("Enter the number of columns"))

for i in range(n):
    row=[]
    for j in range(m):
        num=int(input())
        row.append(num)
    matrices1.append(row)
print(matrices1)



#PART 2

counts=dict()

for i in range(len(matrices1)):
    for j in range(len(matrices1[i])):
        if matrices1[i][j] in counts:
            counts[matrices1[i][j]]+=1
        else:
            if(matrices1[i][j]>0):
                counts[matrices1[i][j]]=1

print(counts)

#part 3
print("Enter the value of matrix 2")
for i in range(n):
    row=[]
    for j in range(m):
        num=int(input())
        row.append(num)
    matrices2.append(row)


#addition 
for i in range(len(matrices1)):
    row=[]
    for j in range(len(matrices1[i])):
        row.append(matrices1[i][j]+matrices2[i][j])
    matrices3.append(row)

print(matrices3)

















# counts3=dict()            
# for i in range(len(matrices3)):
#     for j in range(len(matrices3[i])):
#         if matrices3[i][j] in counts:
#             counts3[matrices3[i][j]]+=1
#         else:
#             counts3[matrices3[i][j]]=1
# print(counts3)