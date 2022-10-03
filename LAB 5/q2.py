class Vechile():

    def __init__(self,owner,vno,manufacturer):
        self.owner=owner
        self.vno=vno
        self.manufacturer=manufacturer


class Passenger(Vechile):
    def __init__(self,owner,vno,manufacturer,nos):
        super().__init__(owner,vno,manufacturer)
        self.nos=nos
        

    def display(self):
        print('The Details are as follows: ')
        print(self.owner,self.vno,self.manufacturer,self.nos)



owner_name=str(input("ENTER OWNER'S NAME: "))
v_no=str(input("Enter VEchile No: "))
manufacturer=str(input("Enter the brand"))
p_no=int(input("Enter the number of passenger: "))
    
p1=Passenger(owner_name,v_no,manufacturer,p_no)
p1.display()
