from django.urls import path, include

from library import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name="index"),
    path(
        'book-create/', views.BookCreateView.as_view(), name="book-create"
    ),
    path(
        'book-list/', views.BookListView.as_view(), name="book-list"
    ),
    path(
        'book-detail/<pk>', views.BookDetailView.as_view(), name="book-detail"
    ),
    path(
        'book-update/<pk>', views.BookUpdateView.as_view(), name="book-update"
    ),
    path(
        'book-delete/<pk>', views.BookDeleteView.as_view(), name="book-delete"
    ),
]