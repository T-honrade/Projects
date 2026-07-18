# views.py

from models import books


def show_books():
    print("\n===== ALL BOOKS =====")

    for i, book in enumerate(books, start=1):
        status = "Borrowed" if book["borrowed"] else "Available"

        print(f"{i}. {book['title']}")
        print(f"   Author: {book['author']}")
        print(f"   Status: {status}")

        if book["borrowed"]:
            print(f"   Borrowed By: {book['borrowed_by']}")

        print()


def borrow_book():
    show_books()

    try:
        choice = int(input("Enter book number to borrow: ")) - 1

        if choice < 0 or choice >= len(books):
            print("Invalid book number.")
            return

        if books[choice]["borrowed"]:
            print("Book is already borrowed.")
            return

        student = input("Student Name: ")

        books[choice]["borrowed"] = True
        books[choice]["borrowed_by"] = student

        print("Book borrowed successfully!")

    except ValueError:
        print("Invalid input.")


def return_book():
    show_books()

    try:
        choice = int(input("Enter book number to return: ")) - 1

        if choice < 0 or choice >= len(books):
            print("Invalid book number.")
            return

        if not books[choice]["borrowed"]:
            print("Book is already available.")
            return

        books[choice]["borrowed"] = False
        books[choice]["borrowed_by"] = ""

        print("Book returned successfully!")

    except ValueError:
        print("Invalid input.")


def show_available_books():
    print("\n===== AVAILABLE BOOKS =====")

    found = False

    for book in books:
        if not book["borrowed"]:
            found = True
            print(f"{book['title']} - {book['author']}")

    if not found:
        print("No available books.")


def show_borrowed_books():
    print("\n===== BORROWED BOOKS =====")

    found = False

    for book in books:
        if book["borrowed"]:
            found = True
            print(f"{book['title']} - Borrowed by {book['borrowed_by']}")

    if not found:
        print("No borrowed books.")


def menu():
    while True:

        print("\n====== LIBRARY BOOK BORROWING SYSTEM ======")
        print("1. Show All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Show Available Books")
        print("5. Show Borrowed Books")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_books()

        elif choice == "2":
            borrow_book()

        elif choice == "3":
            return_book()

        elif choice == "4":
            show_available_books()

        elif choice == "5":
            show_borrowed_books()

        elif choice == "6":
            print("Thank you for using the Library System!")
            break

        else:
            print("Invalid choice.")