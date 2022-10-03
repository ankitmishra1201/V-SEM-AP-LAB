
# Creating a file
file=open("sample.txt","w")
for i in range(8):
    file.write(f"This is line {i} \n")


# Reading a file
file=open("sample.txt","r")
print(file.read())


#Part 3
part3={}
key=1
file=open("sample.txt","r")
for line in file.readlines():
    part3["key"]=key
    part3["String"]=line.strip();
    part3["length"]=len(line);
    key+=1

print(part3)


