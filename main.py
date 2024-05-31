from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


# App Initialization
app = FastAPI()


# Memory
books = [
    {
        "id": 1,
        "title": "hackers",
        "author": "stephen levy",
        "pub_year": 2010,
        "genre": "tech"
    }
]


class Book(BaseModel):
    title: str
    author: str
    pub_year: int
    genre: str


class UpdateBook(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    pub_year: Optional[int] = None
    genre: Optional[int] = None


# home route
@app.get('/')
def test_route():
    return {"Data": "Home Route"}


# Creat new book
@app.post('/create-book')
def create_book(new_book: Book):
    new_book = {
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author,
        "pub_year": new_book.pub_year,
        "genre": new_book.genre
    }
    print(new_book)
    for book in books:
        if book["id"] == new_book["id"]:
            return {"Error": "Book already exists"}

    books.append(new_book)
    return {"Data": books}



# Get all books
@app.get('/get-books')
def get_books():
    return {"Data": books}


# Get a single book
@app.get('/get-book/{book_id}')
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return {"Data": book}
    return {"Error": "Book not found"}


# Update a book
@app.put('/update-book/{book_id}')
def update_book(book_id: int, update_book: UpdateBook):
    for book in books:
        if book["id"] == book_id:
            if update_book.title != None:
                books[book_id]["title"] = update_book.title

            if update_book.author != None:
                books[book_id]["author"] = update_book.author

            if update_book.pub_year != None:
                books[book_id]["pub_year"] = update_book.pub_year
            
            if update_book.genre != None:
                books[book_id]["genre"] = update_book.genre

            return {"Data": books[book_id]}
    return {"Error": "Book not found"}


# Delete Book
@app.delete('/delete-book/{book_id}')
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"Data": books}
    return {"Error": "Book not found"}

