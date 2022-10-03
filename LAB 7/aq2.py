import os

def extsort(files):
    return sorted(files,key=lambda x: os.path.splitext(x)[1])
print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))



def extsort(x):
    i=0
    while(i<len(x)):
         x[i]=x[i].split('.')
         i=i+1
    x.sort(key=lambda x:x[1])
    i=0
    while(i<len(x)):
         x[i]=".".join(x[i])
         i=i+1 
    return x
