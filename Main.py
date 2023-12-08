from Library import Library
from Book import Book

def main():
    library = Library()
    # books added
    library.add_book(Book("Cien años de soledad", "Gabriel García Márquez", 5))
    library.add_book(Book("1984", "George Orwell", 4))
    library.add_book(Book("El señor de los anillos", "J.R.R. Tolkien", 3))
    library.add_book(Book("Harry Potter y la piedra filosofal", "J.K. Rowling", 8))
    library.add_book(Book("Orgullo y Prejuicio", "Jane Austen", 2))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 4))
    library.add_book(Book("El principito", "Antoine de Saint-Exupéry", 5))
    library.add_book(Book("El Gran Gatsby", "F. Scott Fitzgerald", 3))
    library.add_book(Book("Moby Dick", "Herman Melville", 2))
    library.add_book(Book("La Divina Comedia", "Dante Alighieri", 1))

    while True:
        # Menu
        print("\nWelcome to Library")
        print("1. Show Book Catalog")
        print("2. Book loan")
        print("3. Return a book")
        print("4. Late Penalty")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            library.display_catalog()
        elif choice == "2":
            book_title = input("Enter the title of the book you want to borrow: ")
            quantity = int(input("Enter the number of copies you want to borrow: "))
            if library.checkout_book(book_title, quantity):
                print(f"You borrow {quantity} copies(s) of the book '{book_title}'.")
            else:
                print(f"can't borrow the book '{book_title}'.")
        elif choice == "3":
            book_title = input("Enter the title of the book you want to return: ")
            if library.return_book(book_title):
                print(f"Book '{book_title}' returned successfully.")
            else:
                print(f"Can't return the book '{book_title}'.")
        elif choice == "4":
            book_title = input("Enter the title of the book to calculate the fine: ")
            late_fee = library.calculate_late_fee(book_title)
            if late_fee > 0:
                print(f"The Late Fee for the Book '{book_title}' it's ${late_fee}.")
            else:
                print(f"There is no late penalty for the book '{book_title}'.")
        elif choice == "5":
            print("Thanks!")
            break
        else:
            print("Invalid option. Try again")

if __name__ == "__main__":
    main()