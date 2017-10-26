from django import forms

from .models import *


class MinesweepForm(forms.ModelForm):
    class Meta:
        model = Minesweep
        fields = [
            'tooltip', 'tooltip_style',
            'content', 'content_style',
            'width', 'height',
        ]

        widgets = {
            'tooltip_style': forms.Textarea(attrs={'rows': '2'}),
            'content': forms.Textarea(attrs={'rows': '2'}),
            'content_style': forms.Textarea(attrs={'rows': '2'}),
            'tooltip': forms.Textarea(attrs={'rows': '2'})
        }
