from django.urls import path
from .views import IndexView
from .views import search_books

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', search_books, name='search_books'),
]
