class Car:
    def __init__(self,engine,reg,date,colour,model,owner):
        self.engine=engine
        self.reg=reg
        self.date=date
        self.colour=colour
        self.model=model
        self.owner=owner
    def displayCar(self):
        self.owner.displayOwner()
        print("Engine:",self.engine,end=" ")
        print("reg:",self.reg,end=" ")
        print("Date:",self.date,end=" ")
        print("Colour:",self.colour,end=" ")
        print("Model:",self.model,end=" ")
        print()
class Owner:
    def __init__(self,name,address,profession,licenseno):
        self.name=name
        self.address=address
        self.profession=profession
        self.licenseno=licenseno
    def displayOwner(self):
        print("Name:",self.name,end=" ")
        print("Address:",self.address,end=" ")
        print("Profession:",self.profession,end=" ")
        print("LicenseNo:",self.licenseno,end=" ")
        print()
        
n=int(input("Enter number of Owner objects:"))
k=[]
for i in range(n):
    print("Enter name,address,profession,LicenseNo:")
    name=input()
    address=input()
    profession=input()
    LicenseNo=int(input())
    m1=Owner(name,address,profession,LicenseNo)
    k.append(m1)
for i in range(len(k)):
    k[i].displayOwner()
a=[];    
for i in range(2):
    print("Enter engine,reg,date,colour,owner,model:")
    engine=input()
    reg=int(input())
    date=input()
    colour=input()
    model=input()
    m2=Car(engine,reg,date,colour,model,k[i])
    a.append(m2)
for i in range(len(a)):
    a[i].displayCar()
