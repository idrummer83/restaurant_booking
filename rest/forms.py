from django.forms import ModelForm

from rest.models import Table, Visitor


class DateForm(ModelForm):
    class Meta:
        model = Table
        fields = ['table_number', ]
        exclude = ['table_form', 'table_width', 'table_height']


class ConfirmationForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['visitor_table', 'visitor_table_date', 'visitor_name', 'visitor_email']
