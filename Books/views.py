from  django.views.generic import ListView
from .models import Books
# Create your views here.

class BookList(ListView):
    
    model = Books
    template_name = 