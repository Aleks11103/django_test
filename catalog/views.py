from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views.generic import ListView, DetailView


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_aurhors = Author.objects.all().count()
    num_genres = Genre.objects.all().count()
    book_i_in_title = Book.objects.filter(title__contains='и').count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
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
            'num_visits': num_visits,
        }
    )


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 10
    # context_object_name = 'my_book_list'
    # queryset = Book.objects.filter(title__icontains='и')[:5]
    # template_name = 'books/my_arbitrary_template_name_list.html'

    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='')[:5]

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     context['some_data'] = 'This is just some data'
    #     return context
    
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

#Если бы ен использовался class BookDetailView
# def book_detail_view(request,pk):
#     try:
#         book_id=Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")

#     #book_id=get_object_or_404(Book, pk=pk)

#     return render(
#         request,
#         'catalog/book_detail.html',
#         context={'book':book_id,}
#     )


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'