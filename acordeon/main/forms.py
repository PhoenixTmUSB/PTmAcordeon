from django import forms

from .models import *


class AccordionForm(forms.ModelForm):
    panels = forms.IntegerField(label='Paneles extra', min_value=0, required=False)

    class Meta:
        model = Accordion
        fields = [
            'title', 'title_style',
            'content', 'content_style',
            'width', 'height',
            'style', 'panels',
        ]

        widgets = {
            'title_style': forms.Textarea(attrs={'rows': '2'}),
            'content': forms.Textarea(attrs={'rows': '4'}),
            'content_style': forms.Textarea(attrs={'rows': '2'}),
            'style': forms.Textarea(attrs={'rows': '2'})
        }
