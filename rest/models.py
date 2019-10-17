from django.db import models

# Create your models here.


class RestaurantSpace(models.Model):
    rest_width = models.SmallIntegerField(verbose_name='rest width', blank=True, null=True)
    rest_height = models.SmallIntegerField(verbose_name='rest height', blank=True, null=True)

    def __str__(self):
        return 'Rest. Space'

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurant'


TABLE_FORM = (
    ('R', 'Rectangular'),
    ('C', 'Circle'),
)


class Table(models.Model):
    table_number = models.SmallIntegerField(verbose_name='table number')
    table_seats = models.SmallIntegerField(verbose_name='table seats', blank=True)
    table_form = models.CharField(max_length=1, choices=TABLE_FORM, default='Rectangular')
    table_width = models.SmallIntegerField(verbose_name='table width', blank=True, null=True)
    table_height = models.SmallIntegerField(verbose_name='table height', blank=True, null=True)
    table_position_width = models.SmallIntegerField(verbose_name='table position width', blank=True, null=True)
    table_position_height = models.SmallIntegerField(verbose_name='table position height', blank=True, null=True)

    def __str__(self):
        return ('{}').format(self.table_number)

    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'


class Visitor(models.Model):
    visitor_table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='visitor_table')
    visitor_table_date = models.CharField(max_length=10, verbose_name='visitor table date reserve', blank=True, null=True)
    visitor_name = models.CharField(max_length=15, verbose_name='visitor name')
    visitor_email = models.EmailField(max_length=25, verbose_name='visitor email')

    def __str__(self):
        return ('{}-{}').format(self.visitor_table, self.visitor_name)

    class Meta:
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетители'
