from rest_framework import viewsets, generics
from core.models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer

    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        name = self.request.query_params.get("name")
        publication_year = self.request.query_params.get("publication_year")
        edition = self.request.query_params.get("edition")
        author = self.request.query_params.get("author")

        if name:
            queryset = queryset.filter(name__icontains=name)
        if publication_year:
            queryset = queryset.filter(publication_year=publication_year)
        if edition:
            queryset = queryset.filter(edition=edition)
        if author:
            queryset = queryset.filter(authors=author)

        return queryset
