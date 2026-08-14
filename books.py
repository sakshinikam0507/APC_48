books = {
    101: "Python Basics",
    102: "Data Structures",
    103: "Machine Learning"
}

book_id = int(input("Enter book ID to add: "))
book_name = input("Enter book name: ")
books[book_id] = book_name

book_id = int(input("Enter book ID to search: "))

if book_id in books:
    print("Book:", books[book_id])
else:
    print("Book not found")

book_id = int(input("Enter book ID to remove: "))

if book_id in books:
    del books[book_id]

print("Books:")

for book_id, book_name in books.items():
    print(book_id, "-", book_name)

print("Total books:", len(books))
