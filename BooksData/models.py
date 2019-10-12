# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BooksData(models.Model):
    book_name = models.CharField(max_length=100)
