from django.contrib import admin
from rest.models import Table, Visitor, RestaurantSpace

# Register your models here.


@admin.register(RestaurantSpace)
class RestAdmin(admin.ModelAdmin):
    pass


# @admin.register(TableDate)
# class TableDateAdmin(admin.ModelAdmin):
#     list_display = ['table', 'table_date']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'table_form', 'table_width', 'table_height']
    # inlines = TableAdmin


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ['visitor_table', 'visitor_table_date', 'visitor_name', 'visitor_email']