class Books():

    def __init__(self, author, title, price, publisher, copies):
        self.author = author
        self.title = title
        self.price = price
        self.publisher = publisher

        self.copies = copies

    def search_title(self, title):
        if (title == self.title):
            print(self.author, " ", self.title, " ", self.price)

    def search_author(self, author):
        if (author == self.author):
             print("No of copies available= ",)

    def buy_no_of_copies(self, num):
        try:
           if (self.copies == 0):
             raise BookNotAvailable

           elif (num > self.copies):
             raise InsufficientCopies

           else:
             print("Price of book for ", num, "copies is ", self.price*num)
        except BookNotAvailable:
            print("Books Not available")
            exit()
        except InsufficientCopies:
            print("Required copies not in Stock")
            exit()


# Additional Q2
class BookNotAvailable(Exception):
    pass

class InsufficientCopies(Exception):
    pass

b1=Books("Ankit","Life sucks",100,"xyz",0)

n=int(input("Enter the number of copies required"))

b1.buy_no_of_copies(n)



    

