import bookAddView
import bookSearchRemove
import saveLoad
import lentReturn

Books = []
                     
menuText = """
0. Exit
1. Add Book
2. View All Books
3. Search By Title or ISBN
4. Search By Author
5. Remove Book
6. Book Lend
7. Lent Book Information
8. Book Return 
"""

while True:
    saveLoad.load_book(Books)
    print(menuText)
    option = int(input("Enter your choice: "))

    if option == 0:
        break
    elif option == 1:
        Books = bookAddView.book_add(Books)
    elif option == 2:
        bookAddView.view_all_books(Books)
    elif option == 3:
        bookSearchRemove.searchByTitleIsbn(Books)
    elif option == 4:
        bookSearchRemove.searchByAuthor(Books)
    elif option == 5:
        Books = bookSearchRemove.removeBook(Books)
    elif option == 6:
        Books = lentReturn.bookLend(Books)
    elif option == 7:
        lentReturn.viewLentBookInfo()
    elif option == 8:
        Books = lentReturn.bookReturned(Books)




        
