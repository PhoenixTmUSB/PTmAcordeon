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
            'tooltip_side', 'content', 'content_color',
            'content_style', 'width', 'height',
            'border_style', 'border_color', 'border_radius',
            'style'
        ]

        widgets = {
            'tooltip_style': forms.Textarea(attrs={'rows': '1'}),
            'content': forms.Textarea(attrs={'rows': '2'}),
            'content_style': forms.Textarea(attrs={'rows': '2'}),
            'tooltip': forms.Textarea(attrs={'rows': '2'}),
            'border_style': forms.Textarea(attrs={'rows': '2'}),
            'style': forms.Textarea(attrs={'rows': '2'}),
        }