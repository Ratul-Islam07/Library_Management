import saveLoad

def searchByTitleIsbn(Books):
    found_search_result = False 
    search_term = input("Enter Title or ISBN: ").strip()

    for book in Books:
        if search_term.lower() in book["Title"].lower():
           found_search_result = True
           print("Book Found!")
           print(f"{book["Title"]} - {book["Authors"]} - {book["ISBN"]} - {book["Publishing Year"]} - {book["Price"]} - {book["Quantity"]}")

        if search_term.lower() in book["ISBN"].lower():
           found_search_result = True
           print("Book Found!")
           print(f"{book["Title"]} - {book["Authors"]} - {book["ISBN"]} - {book["Publishing Year"]} - {book["Price"]} - {book["Quantity"]}")

    if not found_search_result:
        print("No item found")
        return
    
def searchByAuthor(Books):
    found_search_result = False 
    search_term = input("Enter Author name: ").strip()

    for book in Books:
        if any(search_term.lower() in author.lower() for author in book["Authors"]):
            found_search_result = True
            print("Book Found!")
            print(f'{book["Title"]} - {", ".join(book["Authors"])} - {book["ISBN"]} - {book["Publishing Year"]} - {book["Price"]} - {book["Quantity"]}')
    
    if not found_search_result:
        print("No item found")

def removeBook(Books):
    search_term = input("Enter a book title to search:")
    count = False
    for index,book in enumerate(Books):
        if search_term.lower() == book["Title"].lower():
            count = True
            print(f'Index no: {index+1} | {book["Title"]} - {book["Authors"]} - {book["ISBN"]} - {book["Publishing Year"]} - {book["Price"]} - {book["Quantity"]}')
    if count:    
        selected_index = int(input("Enter an index number to remove: "))
        Books.pop(selected_index - 1)
        print("Book removed successfully!")
        saveLoad.save_book(Books)
        return Books
    else: 
        print("Invalid Book title!")
        return Books 