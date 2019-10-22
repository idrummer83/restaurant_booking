from django.forms import ModelForm
from django import forms

from rest.models import Visitor


class ConfirmationForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['visitor_table', 'visitor_table_date', 'visitor_name', 'visitor_email']
        widgets = {
            'visitor_table': forms.TextInput(attrs={'readonly':'readonly'}),
            'visitor_table_date': forms.TextInput(attrs={'readonly':'readonly'}),
        }