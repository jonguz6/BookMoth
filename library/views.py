from django.shortcuts import render
import django.views.generic as views
from django.urls import reverse_lazy

from library import models, forms


class BookCreateView(views.CreateView):
    model = models.Book
    template_name = "book/book_create_template.html"
    form_class = forms.BookForm
    success_url = reverse_lazy("library:book-list")


class BookListView(views.ListView):
    model = models.Book
    template_name = "book/book_list_template.html"


class BookDetailView(views.DetailView):
    model = models.Book
    template_name = "book/book_detail_template.html"


class BookUpdateView(views.UpdateView):
    model = models.Book
    template_name = "book/book_update_template.html"
    form_class = forms.BookForm
    success_url = reverse_lazy("library:book-list")


class BookDeleteView(views.DeleteView):
    model = models.Book
    template_name = "book/book_delete_template.html"
    success_url = reverse_lazy("library:book-list")


class InventoryCreateView(views.CreateView):
    model = models.Inventory
    template_name = "inventory/inventory_create_template.html"
    form_class = forms.InventoryForm
    success_url = reverse_lazy("library:inventory-list")


class InventoryListView(views.ListView):
    model = models.Inventory
    template_name = "inventory/inventory_list_template.html"


class InventoryDetailView(views.DetailView):
    model = models.Inventory
    template_name = "inventory/inventory_detail_template.html"


class InventoryUpdateView(views.UpdateView):
    model = models.Inventory
    template_name = "inventory/inventory_update_template.html"
    form_class = forms.InventoryForm
    success_url = reverse_lazy("library:inventory-list")


class InventoryDeleteView(views.DeleteView):
    model = models.Inventory
    template_name = "inventory/inventory_delete_template.html"
    success_url = reverse_lazy("library:inventory-list")


def index(request):
    return render(
        request, template_name="book/book_index.html"
    )
