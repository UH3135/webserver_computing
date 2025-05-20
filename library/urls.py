from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>', views.book_history, name='book_history')
]