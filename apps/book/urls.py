# from django.urls import path
# from . import views



# app_name = 'book-url'
# urlpattern = [
#     path('authors/',views.list_authors,name='list-author'),
# ]

from django.urls import path
from . import views

app_name = 'book-url'
#url donesnt understand class but understand function based views only
#when using class base view we need to convert it to function based view as_veiw()
urlpatterns = [
    path('author/', views.list_authors, name='list_authors'),
    path('tag/', views.list_tags, name='list_tags'),
    path('list/', views.list_books, name='list-books'),
    path('create/', views.create_books, name='create-books'),
    path('list/list/', views.BooksView.as_view() , name='class-list-book'),
    path('author/<int:pk>', views.DetailAuthor.as_view(), name='detail-author')
]