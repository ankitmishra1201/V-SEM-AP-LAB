from secrets import choice


class Bank():

    def __init__(self, name, age, accno, acctype, balance):
        self.name = name
        self.age = age
        self.accno = accno
        self.acctype = acctype
        self.balance = balance

    def deposit(self, amount):
        try:
            if (amount > 10000):
                raise DepositError
            else:
                self.balance = self.balance+amount
        except DepositError:
            print("Cant deposit more than Rs 10000")
            exit()

    def withdraw(self, amount):
        if (self.balance >= amount):
            try:
                if (amount > 5000 and self.balance-amount <= 1000):
                    raise WithdrawError
            except WithdrawError:
                print("Withdrawl error")
                exit()

        else:
            print("Invalid Balance")

    def display(self):
        print(" name ", self.name, "\n", "acc-no", self.accno, "\n", "age ",
              self.age, "\n", "acc-type ", self.acctype, "\n", "balance ", self.balance)


# Additional Q1
class BalanceError(Exception):
    pass


class DepositError(Exception):
    pass


class WithdrawError(Exception):
    pass

# Q4


class AgeError(Exception):
    pass


class AccnoError(Exception):
    pass


class AcctypeError(Exception):
    pass


name = str(input("Enter the name"))
age = int(input("Enter age: "))
try:
    if (age < 18 and age > 100):
        raise AgeError
except AgeError:
    print("Age between 18 to 100")
    exit()
accno = int(input("Enter accno: "))
try:
    if (len(str(accno)) != 5):
        raise AccnoError
except AccnoError:
    print("Acc no should be more than 5 digits")
    exit()
acctype = str(input("Enter acctype: "))
# try:
#     if (acctype != "C" or acctype != "S"):
#         raise AcctypeError
# except AcctypeError:
#     print("Acc type should be C or S")
#     exit()
balance = int(input("Enter the Balance: "))
try:
    if (balance < 1000):
        raise BalanceError
except BalanceError:
    print("Balance cant be below 1000")
    exit()


b1 = Bank(name, age, accno, acctype, balance)
while True:
    print("Select Choice ")
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Display")
    print("4) Exit")
    ch=int(input("Enter the choice: "))
    if(ch==1):
        amount=int(input("Enter the amount to be deposited: "))
        b1.deposit(amount)
    elif(ch==2):
        amount=int(input("Enter the amount to be Withdraw: "))
        b1.withdraw(amount)
    elif(ch==3):
        b1.display()
    elif(ch==4):
        exit()
    else:
        print("Invalid Choice")


