from dataclasses import dataclass


@dataclass
class Book:
    title : str
    author: str
    pages: int  
    price: float


    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages."


b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
 


# print(b1.title)
# print(b2.author)
# print(b1 == b3)

 
# b1.title = "Anna Karenina"
# b1.pages = 864
# print(b1.bookinfo())

print(b1.description)
print(b2.description)