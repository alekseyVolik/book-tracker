from django.urls import path

urlpatterns = [
    path('', ),

    path('book/create', name='creating_book'),
    path('book/info/<int:pk>', name='book_info'),
    path('book/list', name='book_list'),

    path('author/create', name='creating_author'),
    path('author/info/<int:pk>', name='author_info'),
    path('author/list', name='author_list'),
]
