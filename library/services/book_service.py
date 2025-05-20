from library.models import Book, BorrowHistory
from django.shortcuts import get_object_or_404


def get_all_books():
    all_books = Book.objects.all()
    if all_books:
        return all_books
    return get_object_or_404

def get_book_by_id(book_id: int):
    book = Book.objects.filter(id=book_id)
    if book:
        return book
    return get_object_or_404

def get_borrow_history_for_book(book: Book):
    history = BorrowHistory.objects.filter(Book=book)
    if history:
        return history
    return get_object_or_404