nums1=[]
nums2=[]

m=int(input("Enter the elements you want to enter in List 1: "))

for i in range(m):
    number=int(input("Enter the Value "))
    nums1.append(number)


n=int(input("Enter the elements you want to enter in List 2: "))
for i in range(n):
    number = int(input("Enter the Value "))
    nums2.append(number)


#Intersection
intersection=[]
for i in range(m):
    for j in range(n):
        if(nums1[i]==nums2[j] and nums1[i] not in intersection):
            intersection.append(nums1[i])

print("union", intersection)


#union
union=[]
for i  in range(m):
    union.append(nums1[i])
for j in range(n):
    union.append(nums2[j])
union=set(union)

print("union", union)

#Difference nums1-nums2
difference=[]
for i in range(m):
    if nums1[i] not in nums2:
        difference.append(nums1[i])

print("difference",difference)



