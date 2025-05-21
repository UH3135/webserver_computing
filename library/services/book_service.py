from library.models import Book, BorrowHistory
from django.shortcuts import get_object_or_404


def get_all_books():
    return Book.objects.all()

def get_book_by_id(book_id: int):
    return Book.objects.get(id=book_id) 

def get_borrow_history_for_book(book: Book):
    return book.borrow_history.all()