books = ["Python Basics", "Data Structures", "Machine Learning"]

new_book = input("Enter a book to add: ")
books.append(new_book)

search_book = input("Enter a book to search: ")

if search_book in books:
    print("Book found")
else:
    print("Book not found")

remove_book = input("Enter a book to remove: ")

if remove_book in books:
    books.remove(remove_book)

print("Books:", books)
print("Total books:", len(books))
