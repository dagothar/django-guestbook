from django.views.generic import ListView
from django.shortcuts import render

from .. import models


class EntryListView(ListView):
    model = models.Entry
    context_object_name = 'entries'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
        return paginate_by

    def get_context_data(self, **kwargs):
        ctx = super(ListView, self).get_context_data(**kwargs)
        ctx['form'] = 'form here'
        return ctx
