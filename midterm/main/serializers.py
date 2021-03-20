from rest_framework import serializers
from main.models import Book, Journal


class BookSerializer(serializers.ModelSerializer):

    title = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_date',)


class JournalSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Journal
        fields = ('type', 'publisher', 'books')