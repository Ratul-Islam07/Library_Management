def save_book(Books):
    with open("Book.csv", "w") as file_pointer:  # Open in write mode to overwrite existing content
        file_pointer.write("Title,Authors,ISBN,Publishing Year,Price,Quantity\n")
        for book in Books:
            authors_str = ",".join(book["Authors"]).strip()  # Join authors with a comma
            line = f'{book["Title"]},{authors_str},{book["ISBN"]},{book["Publishing Year"]},{book["Price"]},{book["Quantity"]}\n'
            file_pointer.write(line)
    
    return Books


def load_book(Books):
    Books.clear()
    with open("Book.csv", "r") as file_pointer:
        lines = file_pointer.readlines()
        
        if not lines:
            print("The file is empty.")
            return Books
        
        lines = lines[1:]  # Skip the header if file is not empty
        
        for line in lines:
            line_splitted = line.strip().split(",")
            
            if len(line_splitted) < 6:
                print(f"Skipping malformed line: {line.strip()}")
                continue
            
            # Extracting fields
            title = line_splitted[0]
            authors = line_splitted[1:-4]  # Extract all author names
            isbn = line_splitted[-4]
            publishing_year = line_splitted[-3]
            price = line_splitted[-2]
            quantity = int(line_splitted[-1])
            
            book = {
                "Title": title,
                "Authors": authors,
                "ISBN": isbn,
                "Publishing Year": publishing_year,
                "Price": price,
                "Quantity": quantity,
            }
            
            Books.append(book)

    return Books

