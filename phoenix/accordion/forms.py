from django import forms

from .models import *


class AccordionForm(forms.ModelForm):
    panels = forms.IntegerField(label='Paneles extra', min_value=0, required=False, initial=0)

    class Meta:
        model = Accordion
        fields = [
            'title', 'title_style',
            'content', 'content_style', 'content_color',
            'border_style', 'border_color', 'border_radius',
            'width', 'height', 'style',
            'panels',
        ]

        widgets = {
            'title_style': forms.Textarea(attrs={'rows': '2'}),
            'content': forms.Textarea(attrs={'rows': '2'}),
            'content_style': forms.Textarea(attrs={'rows': '2'}),
            'border_style': forms.Textarea(attrs={'rows': '2'}),
            'style': forms.Textarea(attrs={'rows': '2'}),
        }
