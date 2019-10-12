from rest_framework import serializers
from .models import BooksData


class BooksDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = BooksData
        fields = '__all__'