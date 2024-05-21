from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
    path('search/', views.search, name='search'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
]