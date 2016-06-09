from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    page_count = models.IntegerField()

    def __str__(self):
        return self.title + ' - ' + self.author
