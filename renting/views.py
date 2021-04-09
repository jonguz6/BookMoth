from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
import django.views.generic as views
from django.urls import reverse_lazy

from renting import models, forms
from library.models import BookInstance


class RentalCreateView(views.CreateView):
    model = models.CurrentRental
    template_name = "rental/rental_create_template.html"
    form_class = forms.RentalForm
    success_url = reverse_lazy("renting:rental-list")


class LockedRentalCreateView(LoginRequiredMixin, views.CreateView):
    model = models.CurrentRental
    template_name = "rental/rental_create_template.html"
    form_class = forms.LockedRentalForm
    success_url = reverse_lazy("renting:rental-list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        book = self.kwargs.get('book_id')
        user = self.request.user
        if book is None:
            return kwargs
        kwargs['initial'] = {'book': BookInstance.objects.filter(book=book, status='A').first(),
                             'profile': models.Profile.objects.get(user=user)}
        return kwargs

    def get(self, request, *args, **kwargs):
        book = kwargs.get('book_id')
        print(book)
        try:
            BookInstance.objects.filter(book=book, status='A').first()
        except BookInstance.DoesNotExist:
            messages.error(request, 'No books available!')
            return redirect(request.META['HTTP_REFERER'])
        return super().get(request, args, kwargs)


class RentalListView(views.ListView):
    model = models.CurrentRental
    template_name = "rental/rental_list_template.html"


class RentalDetailView(views.DetailView):
    model = models.CurrentRental
    template_name = "rental/rental_detail_template.html"


class RentalUpdateView(views.UpdateView):
    model = models.CurrentRental
    template_name = "rental/rental_update_template.html"
    form_class = forms.RentalForm
    success_url = reverse_lazy("renting:rental-list")


class RentalDeleteView(views.DeleteView):
    model = models.CurrentRental
    template_name = "rental/rental_delete_template.html"
    success_url = reverse_lazy("renting:rental-list")


def index(request):
    return render(
        request, template_name="rental/rental_index.html"
    )
