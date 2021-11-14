class Book:
    # the 'init' function is called whe the instance is 
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        #To do: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    
    #To do: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return f'{self.price - (self.price * self._discount):.2f}'
        else:
            return f'{self.price:.2f}'

    def setdiscount(self, amount):
        self._discount = amount

#To do: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# print(b1.getprice())


# print(b2.getprice())
# b2.setdiscount(0.25)
# print(b2.getprice())


print(b2._Book__secret)