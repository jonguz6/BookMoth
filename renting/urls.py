from django.urls import path

from renting import views

app_name = "renting"
urlpatterns = [
    path('', views.index, name="index"),
    path(
        'rental-create/<book_id>', views.LockedRentalCreateView.as_view(), name="rental-create"
    ),
    path(
        'rental-list/', views.RentalListView.as_view(), name="rental-list"
    ),
    path(
        'rental-list/<profile>', views.RentalListView.as_view(), name="user-rental-list"
    ),
    path(
        'rental-list/<book>', views.RentalListView.as_view(), name="book-rental-list"
    ),
    path(
        'rental-detail/<pk>', views.RentalDetailView.as_view(), name="rental-detail"
    ),
    path(
        'rental-update/<pk>', views.RentalUpdateView.as_view(), name="rental-update"
    ),
    path(
        'rental-delete/<pk>', views.RentalDeleteView.as_view(), name="rental-delete"
    )
    ]
