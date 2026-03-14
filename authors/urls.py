from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='author-list'),
    path('create/', views.author_create, name='author-create'),
    path('<int:pk>/', views.author_detail, name='author-detail'),
]