# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BooksData

from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .serializers import BooksDataSerializers


class BooksDataViewSet(ModelViewSet):
    serializer_class = BooksDataSerializers
    queryset = BooksData.objects.all()