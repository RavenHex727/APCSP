books = []
print("Welcome to my digital library! It is a cute project that Ms. Orret came up with!")
response = input("Do you want to add, find, or quit a book? Select A/F/Q ")

if response == "A":
    books.append(input("What book do I want to add? "))

elif response == "F":
    sought_book = input("What book do I want to find? ")
    book_found = False

    for book in books:
        if book == sought_book:
            book_found = True
            print("Book was found in digital library")

    if book_found == False:
        print("Book was not found in digital library")

else:
    books.remove(input("What book do you want to remove? "))