from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

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

    path(
        'book-instance-create/', views.BookInstanceCreateView.as_view(), name="book-instance-create-empty"
    ),
    path(
        'book-instance-create/<book_id>', views.BookInstanceCreateView.as_view(), name="book-instance-create"
    ),
    path(
        'book-instance-list/', views.BookInstanceListView.as_view(), name="book-instance-list"
    ),
    path(
        'book-instance-detail/<pk>', views.BookInstanceDetailView.as_view(), name="book-instance-detail"
    ),
    path(
        'book-instance-update/<pk>', views.BookInstanceUpdateView.as_view(), name="book-instance-update"
    ),
    path(
        'book-instance-delete/<pk>', views.BookInstanceDeleteView.as_view(), name="book-instance-delete"
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
