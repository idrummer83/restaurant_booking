from django.contrib import admin
from rest.models import TableDate, Table, Visitor, Language, Programmer, RestaurantSpace

# Register your models here.


@admin.register(RestaurantSpace)
class RestAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(Programmer)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(TableDate)
class TableDateAdmin(admin.ModelAdmin):
    list_display = ['table', 'table_date']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'table_form', 'table_width', 'table_height']
    # inlines = TableAdmin


@admin.register(Visitor)
class TableAdmin(admin.ModelAdmin):
    list_display = ['visitor_table', 'visitor_name', 'visitor_email']