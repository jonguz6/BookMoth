from django.conf import settings
from django.conf.urls.static import static
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
    
    path(
        'inventory-create/', views.InventoryCreateView.as_view(), name="inventory-create"
    ),
    path(
        'inventory-list/', views.InventoryListView.as_view(), name="inventory-list"
    ),
    path(
        'inventory-detail/<pk>', views.InventoryDetailView.as_view(), name="inventory-detail"
    ),
    path(
        'inventory-update/<pk>', views.InventoryUpdateView.as_view(), name="inventory-update"
    ),
    path(
        'inventory-delete/<pk>', views.InventoryDeleteView.as_view(), name="inventory-delete"
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
