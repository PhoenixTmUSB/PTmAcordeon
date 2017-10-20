from django import forms

from .models import *


class AccordionForm(forms.ModelForm):
    class Meta:
        model = Accordion
        fields = [
            'title', 'title_style',
            'content', 'content_style',
            'width', 'height',
            'style'
        ]

        widgets = {
            'title_style': forms.Textarea(attrs={'rows': '3'}),
            'content_style': forms.Textarea(attrs={'rows': '3'})
        }
