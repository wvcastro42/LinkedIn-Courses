class Publication:
    def __init__(self, title, price) -> None:
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages



class Magazine(Periodical):
    def __init__(self, title, period, publisher, price):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, period, publisher, price) -> None:
        super().__init__(title, price, period, publisher)


b1 = Book("Brave new world", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "NY Times Company", "Daily", 6.0)
m1 = Magazine("Scientific American", "Springer Nature", "Monthly", 5.99)

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)