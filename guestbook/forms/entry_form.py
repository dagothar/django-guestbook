from django.forms import ModelForm
from django.forms import Textarea
from django.forms import TextInput

from .. import models


class EntryForm(ModelForm):
    class Meta:
        model = models.Entry
        fields = [
            'message',
            'author',
        ]
        widgets = {
            'message': Textarea(attrs={
                    'rows': 3,
                    'placeholder': 'Type your message here',
                }),
            'author': TextInput(attrs={
                    'placeholder': 'Your signature here',
                }),
        }
