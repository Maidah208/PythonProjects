# Display menu
def show_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book
def add_book(library):
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == 'yes' else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    for book in library:
        if book['title'].strip().lower() == title:
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search for a book
def search_book(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the title: ").strip().lower()
        results = [b for b in library if title in b['title'].lower()]
    elif choice == "2":
        author = input("Enter the author: ").strip().lower()
        results = [b for b in library if author in b['author'].lower()]
    else:
        print("Invalid choice.")
        return

    if results:
        print("Matching Books:")
        for idx, book in enumerate(results, start=1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("Library is empty.")
        return
    print("Your Library:")
    for idx, book in enumerate(library, start=1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

# Display statistics
def display_stats(library):
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return
    read_books = sum(1 for book in library if book["read"])
    percent_read = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

# Main program
def main():
    library = []

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
