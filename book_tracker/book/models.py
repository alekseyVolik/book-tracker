from django.db import models


class Book(models.Model):
    """This model is representing a book"""

    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    amount = models.IntegerField()
