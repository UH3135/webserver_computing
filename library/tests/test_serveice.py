import pytest
from django.contrib.auth.models import User
from library.models import Book, BorrowHistory
from library.services.book_service import get_book_by_id, get_borrow_history_for_book
from library.exception import BookNotFound, BookHasNoBorrowHistory


@pytest.mark.django_db
def test_get_book_id_success():
    # Given
    book = Book.objects.create(
        title='Test Book',
        author='Tester',
        isbn='12345678'
    )

    # when
    result = get_book_by_id(book.id)

    # Then
    assert result == book
    assert result.title == 'Test Book'


@pytest.mark.django_db
def test_get_book_id_not_found():
    # When & Then
    with pytest.raises(BookNotFound, match="No books found with this ID") as exc_info:
        get_book_by_id(9999)


@pytest.mark.django_db
def test_get_borrow_history_success():
    user = User.objects.create(username='Test')
    book = Book.objects.create(
        title='Test Book',
        author='Tester',
        isbn='12345678'
    )
    history = BorrowHistory.objects.create(
        user=user,
        book=book
    )

    histories = get_borrow_history_for_book(book)

    assert len(histories) == 1
    assert histories[0] == history


@pytest.mark.django_db
def test_get_borrow_history_not_found():
    book = Book.objects.create(title='Empty Book', author='Nobody', isbn='99999999')

    with pytest.raises(BookHasNoBorrowHistory, match='No Histories found with this book') as exec_info:
        get_borrow_history_for_book(book)
