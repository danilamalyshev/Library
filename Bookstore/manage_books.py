def add_book():
    books = []
    while True:
        print("1 to escape")
        a = input("Enter a book title: ")
        books.append(a)
        if a == "1":
            books.pop()
            break

add_book()
