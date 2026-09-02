books={}

def add(book):
    books[book]=True

def issue(book):
    if book in books and books[book]:
        books[book]=False
        print("Book issued")
    else:
        print("Book not available")

def retbook(book):
    if book in books:
        books[book]=True
        print("Book returned")
    else:
        print("Book not found")

def search(book):
    if book in books:
        print("Book found")
    else:
        print("Book not found")

def show():
    for book,ok in books.items():
        if ok:
            print(book)

while True:
    print("1.Add book")
    print("2.Issue book")
    print("3.Return book")
    print("4.Search book")
    print("5.Display available books")
    print("6.Exit")
    ch=int(input("Enter choice: "))

    if ch==1:
        add(input("Enter book name: "))
    elif ch==2:
        issue(input("Enter book name: "))
    elif ch==3:
        retbook(input("Enter book name: "))
    elif ch==4:
        search(input("Enter book name: "))
    elif ch==5:
        show()
    elif ch==6:
        break
