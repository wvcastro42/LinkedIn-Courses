class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name


b1 = Book("War and Peace")
b2 = Book("The Catcher in the Rye")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The NY Times")


print(type(b1))
print(type(n1))

# print(type(b1) == type(b2))
# print(type(b1) == type(n1))

print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n2, object))