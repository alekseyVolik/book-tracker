from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView
)

from .models import (
    Book,
    BookAuthor
)


class BookCreate(CreateView):
    """The view creates a book"""
    model = Book
    fields = ('title', 'author', 'amount')
    success_url = reverse_lazy('book_list')
    template_name = 'book/create.html'


class BookInfo(DetailView):
    """The view displays a book info"""
    model = Book
    template_name = 'book/info.html'


class BookList(ListView):
    """The view displays all books"""
    model = Book
    template_name = 'book/list.html'


class AuthorCreate(CreateView):
    """The view creates an author of book"""
    model = BookAuthor
    fields = ('name', 'surname', 'patronymic')
    success_url = reverse_lazy('author_list')
    template_name = 'author/create.html'


class AuthorInfo(DetailView):
    """The view displays author info"""

    model = BookAuthor
    template_name = 'author/info.html'


class AuthorList(ListView):
    """The view displays all authors"""

    model = BookAuthor
    template_name = 'author/list.html'
