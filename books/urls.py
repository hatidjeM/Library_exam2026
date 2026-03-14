from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('create/', views.book_create, name='book-create'),
    path('<int:pk>/', views.book_detail, name='book-detail'),
    path('<int:pk>/edit/', views.book_edit, name='book-edit'),
    path('<int:pk>/delete/', views.book_delete, name='book-delete'),
]