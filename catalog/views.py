from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_aurhors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    book_i_in_title = Book.objects.filter(title__contains='и').count()
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_aurhors,
            'num_genres': num_genres,
            'book_i_in_title': book_i_in_title,
        }
    )