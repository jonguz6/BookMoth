from django.shortcuts import render
import django.views.generic as views
from django.urls import reverse_lazy

from library import models


class BookCreateView(views.CreateView):
    model = models.Book
    template_name = "book/book_create_template.html"
    fields = "__all__"
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
    fields = "__all__"
    success_url = reverse_lazy("library:book-list")


class BookDeleteView(views.DeleteView):
    model = models.Book
    template_name = "book/book_delete_template.html"
    success_url = reverse_lazy("library:book-list")


def index(request):
    return render(
        request, template_name="book/book_index.html"
    )
