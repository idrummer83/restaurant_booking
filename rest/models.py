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
    # table_date = models.CharField(max_length=10, verbose_name='table date reserve', blank=True, null=True)
    # table_date = models.ManyToManyField(TableDate, on_delete=models.CASCADE, verbose_name='table')
    table_position_width = models.SmallIntegerField(verbose_name='table position width', blank=True, null=True)
    table_position_height = models.SmallIntegerField(verbose_name='table position height', blank=True, null=True)

    def __str__(self):
        return ('{}').format(self.table_number)

    class Meta:
        verbose_name = 'Заказать столик'
        verbose_name_plural = 'Заказать столик'


class TableDate(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='table_date')
    table_date = models.CharField(max_length=10, verbose_name='table date reserve', blank=True, null=True)

    def __str__(self):
        return ('{}').format(self.table_date)

    class Meta:
        verbose_name = 'Table date'
        verbose_name_plural = 'Table date'


class Visitor(models.Model):
    visitor_table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='visitor_table')
    visitor_table_date = models.ForeignKey(TableDate, on_delete=models.CASCADE, related_name='visitor_table_date')
    visitor_name = models.CharField(max_length=15, verbose_name='visitor name')
    visitor_email = models.EmailField(max_length=25, verbose_name='visitor email')

    def __str__(self):
        return ('{}-{}').format(self.visitor_table, self.visitor_name)

    class Meta:
        verbose_name = 'Посетитель'
        verbose_name_plural = 'Посетители'


class Programmer(models.Model):
    name = models.CharField(max_length=15, verbose_name='programmer')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'programmer'


class Language(models.Model):
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=15, verbose_name='language')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'language'
