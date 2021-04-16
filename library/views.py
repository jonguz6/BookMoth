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


class BookInstanceCreateView(views.CreateView):
    model = models.BookInstance
    template_name = "book_instance/book_instance_create_template.html"
    form_class = forms.BookInstanceForm
    success_url = reverse_lazy("library:book-instance-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        book = self.kwargs.get('book_id')
        if book is None:
            return kwargs
        kwargs['initial'] = {'book': models.BookInstance.objects.get(id=book)}
        return kwargs


class BookInstanceListView(views.ListView):
    model = models.BookInstance
    template_name = "book_instance/book_instance_list_template.html"


class BookInstanceDetailView(views.DetailView):
    model = models.BookInstance
    template_name = "book_instance/book_instance_detail_template.html"


class BookInstanceUpdateView(views.UpdateView):
    model = models.BookInstance
    template_name = "book_instance/book_instance_update_template.html"
    form_class = forms.LockedBookInstanceForm
    success_url = reverse_lazy("library:book-instance-list")


class BookInstanceDeleteView(views.DeleteView):
    model = models.BookInstance
    template_name = "book_instance/book_instance_delete_template.html"
    success_url = reverse_lazy("library:book-instance-list")
    
    
def index(request):
    return render(
        request, template_name="book/book_index.html"
    )
