from rest_framework import serializers
from .models import Book
from .models import Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'price']
        read_only_fields = ['id']

class AuthorSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Author
        fields = '__all__'