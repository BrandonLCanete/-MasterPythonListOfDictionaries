# List of book dictionaries
book_list_dictionaries = [
    {
        "book_id" : 1,
        "book_title" : "GO Programming in easy steps",
        "book_author" : "Mike McGrath",
        "book_genre" : "Paperback · Non-fiction · Computer",
        "book_price" : "839.00"
    },
    {
        "book_id" : 2,
        "book_title" : "Web Coding & Development All-in-one For Dummies",
        "book_author" : "Paul McFedries",
        "book_genre" : "Non-fiction · Computer",
        "book_price" : "2,530.40"
    },
    {
        "book_id" : 3,
        "book_title" : "Effective Java",
        "book_author" : "Joshua Bloch",
        "book_genre" : "Paperback · Non-fiction · Business/Economics",
        "book_price" : "1,149.74"
    },
    {
        "book_id" : 4,
        "book_title" : "Logic Primer, third edition",
        "book_author" : "Colin Allen and Michael Hand",
        "book_genre" : "Paperback · Non-fiction · Mathematics",
        "book_price" : "1,919.32"
    },
    {
        "book_id" : 5,
        "book_title" : "Logically Fallacious",
        "book_author" : "Bo Bennett",
        "book_genre" : "Paperback · Non-fiction · Education",
        "book_price" : "1,441.51"
    }
]
# Loop through the list of dictionaries
for books in book_list_dictionaries:
    # Print the data
    print(f"Book Title: {books['book_title']}, Book Author: {books['book_author']}, Book Genre: {books['book_genre']}, Book Price: {books['book_price']}")