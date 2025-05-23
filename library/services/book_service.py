from library.models import Book, BorrowHistory
from library.exception import BookNotFound, BookHasNoBorrowHistory
from django.shortcuts import get_object_or_404


def get_all_books():
    return Book.objects.all()

def get_book_by_id(book_id: int):
    try:
        return Book.objects.get(id=book_id) 
    except Book.DoesNotExist:
        raise BookNotFound(f"No books found with this ID {book_id}")

def get_borrow_history_for_book(book: Book):
    histories = book.borrow_history.order_by('-borrowed_at')
    if not histories:
        raise BookHasNoBorrowHistory(f"No Histories found with this book {book.title}")
    return histories