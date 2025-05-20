from django.shortcuts import render
from library.services import book_service


def book_list(request):
    books = book_service.get_all_books()
    return render(request, 'library/book_list.html', {'books': books})

def book_history(request, book_id):
    book = book_service.get_book_by_id(book_id)
    histories = book_service.get_borrow_history_for_book(book)
    return render(request, 'library/book_history.html', {
        'book': book,
        'histories': histories
    })