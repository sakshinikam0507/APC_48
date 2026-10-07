import csv
import os
books = "books.csv"
def add_book():
    data = [input("book id "), input("Title: ")]
    with open(books, "a", newline="") as f:
        csv.writer(f)
def show_books():
    if os.path.exists(books):
        with open(books) as f:
            for row in csv.reader(f):
                print(row)
    else:
        print("No books found")
while True:
    print("\n1.Add Book  2.Show Books ")
    choice = input("Choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        break
    else:
        print("Wrong choice")
