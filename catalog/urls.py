from django.urls import path
from . import views
from django.conf.urls import url


# urlpatterns = [
#     path('', views.index, name='index'),
# ]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book_detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author_detail'),
    # url(r'^book/\d{4}_\d{2}_\d{2}$', views.BookDateView.as_view(), name='book_date_view'),
    # url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    # url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),
]
