import saveLoad

def book_add(Books):
    title = input("Enter book title: ").strip()
    
    authors = []
    while True:
        author = input("Enter author name (or type 'Done' to finish): ").strip()
        if author.lower() == 'done':
            break
        authors.append(author.strip())

    isbn = input("Enter ISBN number: ").strip()
    publishing_year = input("Enter publishing year: ").strip()
    price = input("Enter price: ").strip()
    quantity = int(input("Enter quantity: ").strip())

    book = {
        "Title": title,
        "Authors": authors,
        "ISBN": isbn,
        "Publishing Year": publishing_year,
        "Price": price,
        "Quantity": quantity,
    }

    Books.append(book)
    
    print("Book added successfully!")
    saveLoad.save_book(Books) 
    return Books 

def view_all_books(Books):
    if not Books:
        print("No books available.")
        return
    print("All the books are shown below: ")
    for i,book in enumerate(Books):
        print("Book No:",i+1, end="")
        print(
            "\nTitle:", book["Title"],
            "\nAuthors:", ", ".join(book["Authors"]),
            "\nISBN:", book["ISBN"],
            "\nPublishing Year:", book["Publishing Year"],
            "\nPrice:", book["Price"],
            "\nQuantity:", book["Quantity"],
            "\n"
        )