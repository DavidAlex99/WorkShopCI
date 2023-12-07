class Book:
    # self: referese to itself
    # author: name of the author of book
    # title: title name of the book
    # copies: number of the same book
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
