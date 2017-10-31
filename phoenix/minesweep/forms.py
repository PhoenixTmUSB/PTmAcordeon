from django import forms

from .models import *


class MinesweepForm(forms.ModelForm):
    SIDE_CHOICES = (
        ('top', 'arriba'),
        ('bottom', 'abajo'),
        ('right', 'derecha'),
        ('left', 'izquierda'),
    )
    tooltip_side = forms.ChoiceField(required=False, choices=SIDE_CHOICES)

    class Meta:
        model = Minesweep
        fields = [
            'tooltip', 'tooltip_style',
            'tooltip_side', 'content',
            'content_style', 'width',
            'height',
        ]

        widgets = {
            'tooltip_style': forms.Textarea(attrs={'rows': '2'}),
            'content': forms.Textarea(attrs={'rows': '2'}),
            'content_style': forms.Textarea(attrs={'rows': '2'}),
            'tooltip': forms.Textarea(attrs={'rows': '2'}),
        }
