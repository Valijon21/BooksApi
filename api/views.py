import imp
from rest_framework.generics import ListAPIView
from Books.models import Books
from .serializers import BooksSerializer

class BooksAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    