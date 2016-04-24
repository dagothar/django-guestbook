from django.views.generic import ListView
from django.shortcuts import render

from .. import models
from ..forms import EntryForm
from paginate_by_mixin import PaginateByMixin


class EntryListView(PaginateByMixin, ListView):
    model = models.Entry
    context_object_name = 'entries'
    ordering = ['-date']
    paginate_by = 3

    form = EntryForm()

    def get_ordering(self):
        """Allows customizing sorting"""
        return self.ordering

    def get_context_data(self, **kwargs):
        """Adds form data to the context"""
        ctx = super(ListView, self).get_context_data(**kwargs)
        ctx['form'] = self.form
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
