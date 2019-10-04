from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.forms import modelformset_factory, inlineformset_factory
from django.db import transaction, IntegrityError
from datetime import datetime


from .forms import DateForm, ConfirmationForm
from .models import Table,Language, Programmer, RestaurantSpace

# Create your views here.


def index(request, programmer_id):
    programmer = Programmer.objects.get(pk=programmer_id)
    # LanguageFormset = modelformset_factory(Language, fields=('name',))
    LanguageFormset = inlineformset_factory(Programmer, Language, fields=('name',), extra=1)

    if request.method == 'POST':
        # formset = LanguageFormset(request.POST, queryset=Language.objects.filter(programmer_id=programmer_id))
        formset = LanguageFormset(request.POST, instance=programmer)
        if formset.is_valid():
            formset.save()
            # instances = formset.save(commit=False)
            # for inst in instances:
            #     inst.programmer_id = programmer.id
            #     inst.save()
            return redirect('index', programmer_id=programmer.id)

    # formset = LanguageFormset(queryset=Language.objects.filter(programmer_id=programmer_id))
    formset = LanguageFormset(instance=programmer)
    return render(request, 'test.html', {
        'formset': formset
    })


def main_page(request):
    restaurant = RestaurantSpace.objects.all().first()
    all_tables = Table.objects.all()
    now = datetime.now()
    context = {
        'restaurant': restaurant,
        'all_tables': all_tables,
        'today': now.strftime('%d/%m/%Y')
    }
    return render(request, 'index.html', context)


def form_table(request, pk):
    all_tables = Table.objects.all()
    table = Table.objects.filter(id=pk).first()
    form = DateForm(request.POST or None, instance=table)
    if form.is_valid():
        table.table_number = table.table_number
        form.save()
        return redirect('/confirm/{}'.format(pk))
    context = {
        'form': form,
        'all_tables': all_tables
    }
    return render(request, 'form.html', context)


def booking_table(request, pk):
    all_tables = Table.objects.all()
    table = Table.objects.filter(id=pk).first()
    form = DateForm(request.POST or None, instance=table)
    if form.is_valid():
        table.table_number = table.table_number
        form.save()
        return redirect('/confirm/{}'.format(pk))
    context = {
        'form': form,
        'all_tables': all_tables
    }
    return render(request, 'form.html', context)


def email_confirmation(request, pk):
    table = Table.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = ConfirmationForm(request.POST or None)
        if form.is_valid():
            receiver_email = form.cleaned_data['visitor_email']
            send_mail('Table confirmation',
                      'Your table is - {}, date is - {}'.format(table.table_number, table.table_date),
                      'email_sender@gmail.com', [receiver_email],
                      fail_silently=False)
            form.save()
            return redirect('/')
    else:
        form = ConfirmationForm()
        context = {
            'form': form,
            'table_id': pk
        }
        return render(request, 'email_confirmation.html', context)