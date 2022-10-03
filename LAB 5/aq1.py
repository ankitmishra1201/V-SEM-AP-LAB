import random
class Employee:
    salary=0
    def __init__(self,id,name,salary,department):
        self.id=id
        self.name=name
        self.salary=salary
        self.department=department
    def __del__(self):
        print("Refernce to "+self.name+" has been deleted")
    def display(self):
        print("Employees id:",self.id)
        print("Employees name:",self.name)
        print("Employees salary:",self.salary)
        print("Employees department:",self.department)
        print("Total salary of all employees:",Employee.salary)
    
        
    @classmethod
    def TotalSalary(cls,salary):
        cls.salary=cls.salary+salary
        
        



n=int(input("Enter number of Employees:"))
k=[]
for i in range(n):
    print("Enter name,salary and department of ",i+1,"th Employee")
    id1=random.randint(2912,8000)
    print(id1)
    name1=input()
    salary1=int(input())
    department1=input()
    j=Employee(id1,name1,salary1,department1)
    Employee.TotalSalary(salary1)
    k.append(j)
q=int(input("Enter user id to be searched:"))
c=0
for i in range(n):
      if (q==k[i].id):
          c=c+1
          k[i].display()
      
if(c==0):
      print("User id not found")
    