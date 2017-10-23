from django import forms

from .models import *

# Create your forms here

class MinesweepForm(forms.ModelForm):
	class Meta:
		model = Minesweep
		fields = [
			'content', 'content_style',
			'width', 'height',
		]