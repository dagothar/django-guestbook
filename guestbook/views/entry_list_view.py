from django.views.generic import ListView
from django.shortcuts import render

from .. import models
from ..forms import EntryForm
from parametrized_pagination_mixin import ParametrizedPaginationMixin


class EntryListView(ParametrizedPaginationMixin, ListView):
    model = models.Entry
    context_object_name = 'entries'
    ordering = ['-date']
    paginate_by = 3
    order = '-date'
    filter = ''

    form = EntryForm()

    def get_queryset(self):
        """Filters the queried objects by the author"""
        objects = super(ListView, self).get_queryset()
        if 'filter' in self.request.GET:
            self.filter = self.request.GET['filter']
        if self.filter:
            objects = objects.filter(author__contains=self.filter)
        return objects

    def get_ordering(self):
        """Allows to customize sorting order"""
        if 'order' in self.request.GET:
            self.order = self.request.GET['order']
        return self.order

    def get_context_data(self, **kwargs):
        ctx = super(ListView, self).get_context_data(**kwargs)
        ctx['form'] = self.form
        ctx['filter'] = self.filter
        ctx['order'] = self.order
        return ctx

    def post(self, request):
        """Processes the new entry form
        If the form is valid, the new entry is saved, and the form is reset
        """
        self.form = EntryForm(request.POST)
        if self.form.is_valid():
            new_entry = self.form.save()
            self.form = EntryForm()

        return self.get(request)
