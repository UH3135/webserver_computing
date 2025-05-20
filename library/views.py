from django.shortcuts import render
from library.services import book_service


def book_list(request):
    books = book_service.get_all_books()
    return render(request, 'library/book_list.html', {'book': books})