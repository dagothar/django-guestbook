from django.forms import ModelForm
from django.forms import Textarea

from .. import models


class EntryForm(ModelForm):
    class Meta:
        model = models.Entry
        fields = [
            'message',
            'author',
        ]
        widgets = {
            'message': Textarea(attrs={'rows': 3})
        }
