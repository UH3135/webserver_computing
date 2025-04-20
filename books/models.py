from django.db import models
from django.db.models import QuerySet

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    @classmethod
    def get_all_books(cls) -> QuerySet['Book']:
        return cls.objects.all()

    @classmethod
    def get_books_by_author(cls, author) -> QuerySet['Book']:
        if author is None:
            return 
        return cls.objects.filter(author=author)

    @classmethod
    def get_books_by_title_keyword(cls, keyword) -> QuerySet['Book']:
        if keyword is None:
            return 
        return cls.objects.filter(title__iexact=keyword)
    
    @classmethod
    def get_books_ordered_by_title(cls) -> QuerySet['Book']:
        return cls.objects.all().order_by('title')