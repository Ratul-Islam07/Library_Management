import saveLoad

def bookLend(Books):
    lent = input("Enter a book title to lent: ")

    for book in Books:
        if lent.lower() == book["Title"].lower():
            if book["Quantity"] > 0:
                book["Quantity"] -= 1
                lender = input("Enter lenders name: ")
                lender_id = input("Enter lenders id: ")
                with open("lender_info.csv", "a") as file_pointer:
                    line = f"{book["Title"]} -- {lender} -- {lender_id}\n"
                    file_pointer.write(line)
                print("Book lent successfully!")
                print(f"Available books : {book["Quantity"]}")
                saveLoad.save_book(Books)
                return Books 
        
        
    print("Book not found!")

def viewLentBookInfo():
    with open("lender_info.csv", "r") as file_pointer:
        lines = file_pointer.readlines()
        if lines:
            print("Lent Books Information:")
            for line in lines:
                if " -- " in line:  # Ensure the line has the expected delimiter
                    title, lender, lender_id = line.strip().split(" -- ")
                    print(f"Title: {title}, Lender: {lender}, Lender ID: {lender_id}")
                else:
                    print("No books have been lent yet.")

def bookReturned(Books):
    book_return = input("Enter book title to be returned: ")
    count = False
    for book in Books:
        if book_return.lower() == book["Title"].lower():
            book["Quantity"] += 1
            count = True
            print("Book returned successfully!")
            print(f"Available books : {book["Quantity"]}")
            saveLoad.save_book(Books) 
            return Books

    if not count:
        print("Invalid Book Title!")
        return Books 
        

    