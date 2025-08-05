from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]