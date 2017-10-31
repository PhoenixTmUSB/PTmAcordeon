from django import forms

from .models import *


class TabForm(forms.ModelForm):
    class Meta:
        model = Tab
        fields = [
            'title', 'title_style',
            'content', 'content_style',
            'width', 'height',
        ]

        widgets = {
            'title_style': forms.Textarea(attrs={'rows': '2'}),
            'content': forms.Textarea(attrs={'rows': '2'}),
            'content_style': forms.Textarea(attrs={'rows': '2'}),
        }
