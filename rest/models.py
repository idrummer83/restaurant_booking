from django.db import models

# Create your models here.

class Table(models.Model):
    TABLE_FORM = (
        ('R', 'Rectangular'),
        ('O', 'Oval'),
    )
    table_number = models.SmallIntegerField(verbose_name='table number')
    table_seats = models.SmallIntegerField(verbose_name='table seats', blank=True)
    table_form = models.CharField(max_length=1, choices=TABLE_FORM, blank=True, null=True)
    table_width = models.SmallIntegerField(verbose_name='table width', blank=True, null=True)
    table_height = models.SmallIntegerField(verbose_name='table height', blank=True, null=True)
    table_date = models.CharField(max_length=10, verbose_name='table date reserve', blank=True, null=True)

    def __str__(self):
        return ('{}').format(self.table_number)

    class Meta:
        verbose_name = 'Заказать столик'
        verbose_name_plural = 'Заказать столик'


class Visitor(models.Model):
    visitor_table = models.SmallIntegerField(verbose_name='visitor table number')
    visitor_name = models.CharField(max_length=15, verbose_name='visitor name')
    visitor_email = models.EmailField(max_length=25, verbose_name='visitor email')

    def __str__(self):
        return ('{}-{}').format(self.visitor_table, self.visitor_name)

    class Meta:
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетители'