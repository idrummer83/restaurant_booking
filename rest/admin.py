from django.contrib import admin
from rest.models import Table, Visitor

# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'table_form', 'table_width', 'table_height', 'table_date']


@admin.register(Visitor)
class TableAdmin(admin.ModelAdmin):
    list_display = ['visitor_table', 'visitor_name', 'visitor_email']