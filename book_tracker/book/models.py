from django.db import models


class Book(models.Model):
    """This model is representing a book"""

    title = models.CharField(max_length=60)
    author = models.ForeignKey('BookAuthor', on_delete=models.PROTECT)
    amount = models.IntegerField()


class BookAuthor(models.Model):
    """This model is representing a book`s author"""

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
