import sqlite3
from sqlite3.dbapi2 import Cursor
conn = sqlite3.connect("employee.db")
print("Openned Database Successfully")
createTableQuery ="CREATE TABLE  EMPLOYEE  (ID TEXT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, ROLE TEXT NOT NULL, SALARY TEXT )"
conn.execute(createTableQuery)
print("Table Created Succesfully")

ch = - 1

def display():
    displayQuery = "SELECT ID, NAME, ROLE, SALARY  FROM EMPLOYEE"
    cursor=conn.execute(displayQuery)
    print(cursor)
    for row in cursor:
            print("ID: "+ row[0]+ " "+ "NAME: "+ row[1]+ " "+ "ROLE:"+" "+row[2]+" "+ "SALARY:" +" "+ row[3])
    print("Operation Done Succesfully")

def insert( ID, NAME, ROLE, SALARY):
    insertQuery="INSERT INTO EMPLOYEE (ID,NAME,ROLE,SALARY) VALUES("+ "'" +ID +"',  '" +  NAME+"', " + "'"+ROLE+"', " +" '"+ SALARY+"'" ")"
    print(insertQuery)
    conn.execute(insertQuery)
    conn.commit()
    print("Operation Done Succesfully")

def checkId(id):
    curr=conn.execute("SELECT NAME FROM EMPLOYEE WHERE ID='"+id+"'")
    count =0
    for r in curr:
        count+=1
    return count

def update(id, place, val):
    updateQuery=" UPDATE EMPLOYEE SET "+" "+place+ val +" "+ "WHERE ID="+ id
    print(updateQuery)
    conn.execute(updateQuery)
    conn.commit()
    print("Operation Done Succesfully")
def delete(id):
    if(checkId(id)==0):
        print("Record Doesn't Exist")
        return
    else:
        deleteQuery="DELETE FROM EMPLOYEE WHERE ID='"+id+"'"
        print(deleteQuery)
        conn.execute(deleteQuery)



while ch is not str(4):
    print("Enter 0 to DISPLAY EMPLOYEE")
    print("Enter 1 to INSERT IN EMPLOYEE")
    print("Enter 2 to UPDATE IN EMPLOYEE")
    print("Enter 3 to DELETE IN EMPLOYEE")
    print("Enter 4 to EXIT IN EMPLOYEE")
    print("Enter Choice:")
    ch=input()
    if ch == str(0):
        display()
    if ch == str(1):
        print("Enter ID:")
        ID = input()
        print("Enter Name:")
        Name = input()
        print("Enter ROLE")
        ROLE= input()
        print("Enter SALARY")
        SALARY= input()
        insert(ID,Name,ROLE,SALARY)
        print()
    if ch ==str(2):
        place=input("Enter Field to be updated:\n")
        place=place+"="
        val = input("Enter filed value:\n")
        val="'"+val+"'"
        id=input("Enter ID:\n")
        id="'"+id+"'"
        update(id,place,val)
        print()
    if ch==str(3):
        id= input("Enter ID to be deleted\n")
        delete(id)
    if ch ==str(4):
      print("Terminate!")
      break