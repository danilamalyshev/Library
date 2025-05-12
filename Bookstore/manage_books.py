def books_manager():
    books = []
    print("Press 1 to add a book or 0 to quit ")
    while (True):

        choice = input('1/0: ')
        if choice == '1':
            bookname = (input("Enter book name: "))
            books.append(bookname)
        elif choice == '0':
            break


books_manager()
#fgfgfgfgfggffggf