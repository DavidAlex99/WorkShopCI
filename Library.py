import Book

def __init__(self):
    # List fo books
    self.books = []
    # Dictionay of books
    self.checked_out_books = {}
def add_book(self, book):
        self.books.append(book)

def display_catalog(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, Copies Available: {book.copies}")

def checkout_book(self, title, quantity):
    # Check if the quantity is a positive integer
    if not isinstance(quantity, int) or quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        return False

    # Find the book in the catalog
    for book in self.books:
        if book.title == title:
            # Check if the book is available in the desired quantity
            if book.copies >= quantity:
                # Update the library catalog
                book.copies -= quantity
                due_date = datetime.datetime.today() + datetime.timedelta(days=14)
                self.checked_out_books[title] = due_date

                print(f"Book '{title}' checked out. Due date: {due_date.strftime('%Y-%m-%d')}")
                return True
            else:
                print(f"Error: Only {book.copies} copies of '{title}' are available.")
                return False

    print(f"Error: Book '{title}' not found in the library.")
    return False

    # Implement checkout logic here
def return_book(self, title):
    # Check if the book is in the checked out list
    if title in self.checked_out_books:
        due_date = self.checked_out_books[title]
        current_date = datetime.datetime.today()
        late_days = (current_date - due_date).days

        # Calculate late fee if any
        late_fee = max(0, late_days) * 1  # $1 per day

        # Find the book in the catalog and update its quantity
        for book in self.books:
            if book.title == title:
                book.copies += 1
                break

        # Remove the book from checked out list
        del self.checked_out_books[title]

        if late_days > 0:
            print(f"Book '{title}' returned with {late_days} days late. Late fee: ${late_fee}")
        else:
            print(f"Book '{title}' returned on time. No late fee.")

        return late_fee
    else:
        print(f"Error: Book '{title}' was not checked out.")
        return 0
#end of method return_book


def calculate_due_date(self):
    # The standard loan period is 14 days
    standard_loan_period = 14
    today = datetime.datetime.today()
    due_date = today + datetime.timedelta(days=standard_loan_period)
    return due_date

def calculate_late_fee(self, title):
    if title in self.checked_out_books:
        due_date = self.checked_out_books[title]
        current_date = datetime.datetime.today()
        late_days = (current_date - due_date).days

        # Calculate late fee, $1 per day for each day overdue
        late_fee = max(0, late_days) * 1
        return late_fee
    else:
        print(f"Error: Book '{title}' was not checked out.")
        return 0


# Implement late fee calculation here


#book selectio and checkout



