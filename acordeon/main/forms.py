from django.forms import ModelForm

from .models import *

class AccordionForm(ModelForm):
    class Meta:
        model = Accordion
        fields = ['name', 'title', 'title_style', 'content', 'content_style',
                  'width', 'height', 'style']