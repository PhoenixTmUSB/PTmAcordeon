from django import forms

from .models import *


class TabForm(forms.ModelForm):

    number_tabs = forms.IntegerField(
        label='Numero de Tabs',
        min_value=1,
        required=False,
        initial=1
    )

    class Meta:
        model = Tab
        fields = [
            'title', 'title_style',
            'content', 'content_style', 'content_color',
            'border_style', 'border_color', 'border_radius',
            'width', 'height', 'style'
        ]

        widgets = {
            'title_style': forms.Textarea(attrs={'rows': '2'}),
            'content': forms.Textarea(attrs={'rows': '2'}),
            'content_style': forms.Textarea(attrs={'rows': '2'}),
            'border_style': forms.Textarea(attrs={'rows': '2'}),
            'style': forms.Textarea(attrs={'rows': '2'}),
        }
