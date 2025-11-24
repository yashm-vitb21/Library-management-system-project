
# Library Book Management System (Python Project)


library = []
issued_books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book_id = len(library) + 1

    library.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    })

    print(f"Book '{title}' added successfully!")

def view_books():
    if not library:
        print("No books in library.")
        return

    print("\n------------- Available Books -------------")
    for book in library:
        status = "Available" if book["available"] else "Issued"
        print(f"ID: {book['id']} | {book['title']} by {book['author']} | {status}")
    print("-------------------------------------------")

def issue_book():
    view_books()
    try:
        book_id = int(input("Enter book ID to issue: "))
    except ValueError:
        print("Invalid ID!")
        return

    for book in library:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                issued_books.append(book)
                print(f"Book '{book['title']}' issued successfully!")
            else:
                print("Book is already issued.")
            return

    print("Book not found!")

def return_book():
    if not issued_books:
        print("No books are issued currently.")
        return

    print("\n----------- Issued Books -----------")
    for book in issued_books:
        print(f"ID: {book['id']} | {book['title']} by {book['author']}")
    print("------------------------------------")

    try:
        book_id = int(input("Enter book ID to return: "))
    except ValueError:
        print("Invalid ID!")
        return

    for book in issued_books:
        if book["id"] == book_id:
            book["available"] = True
            issued_books.remove(book)
            print(f"Book '{book['title']}' returned successfully!")
            return

    print("Book not found in issued list!")

def main():
    print("============================================")
    print("        LIBRARY BOOK MANAGEMENT SYSTEM      ")
    print("============================================")

    while True:
        print("\n1. Add Book")
        print("2. View All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid option! Try again.")

main()

