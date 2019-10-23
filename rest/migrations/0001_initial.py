# Generated by Django 2.2.4 on 2019-09-18 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='programmer')),
            ],
            options={
                'verbose_name': 'programmer',
            },
        ),
        migrations.CreateModel(
            name='RestaurantSpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_width', models.SmallIntegerField(blank=True, null=True, verbose_name='rest width')),
                ('rest_height', models.SmallIntegerField(blank=True, null=True, verbose_name='rest height')),
            ],
            options={
                'verbose_name': 'Restaurant',
                'verbose_name_plural': 'Restaurant',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.SmallIntegerField(verbose_name='table number')),
                ('table_seats', models.SmallIntegerField(blank=True, verbose_name='table seats')),
                ('table_form', models.CharField(choices=[('R', 'Rectangular'), ('C', 'Circle')], default='Rectangular', max_length=1)),
                ('table_width', models.SmallIntegerField(blank=True, null=True, verbose_name='table width')),
                ('table_height', models.SmallIntegerField(blank=True, null=True, verbose_name='table height')),
                ('table_position_width', models.SmallIntegerField(blank=True, null=True, verbose_name='table position width')),
                ('table_position_height', models.SmallIntegerField(blank=True, null=True, verbose_name='table position height')),
            ],
            options={
                'verbose_name': 'Заказать столик',
                'verbose_name_plural': 'Заказать столик',
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_table', models.SmallIntegerField(verbose_name='visitor table number')),
                ('visitor_name', models.CharField(max_length=15, verbose_name='visitor name')),
                ('visitor_email', models.EmailField(max_length=25, verbose_name='visitor email')),
            ],
            options={
                'verbose_name': 'Посетитель',
                'verbose_name_plural': 'Посетители',
            },
        ),
        migrations.CreateModel(
            name='TableDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_date', models.CharField(blank=True, max_length=10, null=True, verbose_name='table date reserve')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_date', to='rest.Table')),
            ],
            options={
                'verbose_name': 'Table date',
                'verbose_name_plural': 'Table date',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='language')),
                ('programmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.Programmer')),
            ],
            options={
                'verbose_name': 'language',
            },
        ),
    ]