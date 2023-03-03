from django.urls import path

from .views import (
    AuthorInfo,
    AuthorCreate,
    AuthorList,
    BookInfo,
    BookCreate,
    BookList
)

urlpatterns = [
    path('book/create', BookCreate.as_view(), name='creating_book'),
    path('book/info/<int:pk>', BookInfo.as_view(), name='book_info'),
    path('book/list', BookList.as_view(), name='book_list'),

    path('author/create', AuthorCreate.as_view(), name='creating_author'),
    path('author/info/<int:pk>', AuthorInfo.as_view(), name='author_info'),
    path('author/list', AuthorList.as_view(), name='author_list'),
]
